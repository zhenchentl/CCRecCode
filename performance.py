#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: performance.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月15日 星期四 20时15分49秒
#########################################################################

import sys
sys.path.append('..')
from util.Params import *
from redisHelper.RedisHelper import RedisHelper
import re

def getRecomList():
    recom_list_all = []
    with open(RECOM_LIST_PATH) as file_input:
        for line in file_input:
            recom_list = []
#             s = re.sub("[^a-zA-Z,.]", " ", line)
            p1 = re.compile('(, [0-9]+.[0-9]+\), \()')
            s = p1.sub(',', line)
            p2 = re.compile('(\[|\]|\(|\))|\'')
            s = p2.sub('', s)
            recom_list = s.split(':')[1].split(',')
            recom_list.pop(0)
            recom_list_all.extend(recom_list[0:ReconListSize])
    file_input.close()
    return recom_list_all

def getTargetNodes():
    with open(FILE_PATH_TARGETNODES) as file_input:
        targetNodes = file_input.readline().strip().split(',')
    return targetNodes

def getCoauthorList():
    targeNodes = getTargetNodes()
    mRedisHelper = RedisHelper()
    coauthorList_all = []
    print targeNodes
    for targetNode in targeNodes:
        coauthorList = []
        coauthorList = list(mRedisHelper.getCoauthors(targetNode))
        coauthorList_all.extend(coauthorList)
    return coauthorList_all
if __name__ == '__main__':
    RecomList = list(getRecomList())
    CoauthorList = list(getCoauthorList())
    countA = 0
    for recomNode in RecomList:
        for coauthor in CoauthorList:
            if recomNode == coauthor:
                countA += 1
    precision = countA * 1.0 / len(RecomList)
    recall = countA * 1.0 / len(CoauthorList)
    print 'precision:' + str(precision)
    print 'recall:' + str(recall)
    
    print 'F1:' + str(2.0 * precision * recall/(precision + recall))