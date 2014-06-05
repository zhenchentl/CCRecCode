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

def getRecomList(TopN = 15):
    recom_list_all = []
    with open(RECOM_LIST_PATH_ACREC) as file_input:
        for line in file_input:
#             print line
            recom_list = []
#             s = re.sub("[^a-zA-Z,.]", " ", line)
            p1 = re.compile('(, [0-9]+.[0-9]+\), \()')
            s = p1.sub(',', line)
#             print s
            p2 = re.compile('(, [0-9]+.[0-9]+e-[0-9]+\), \()')
            s = p2.sub(',', s)
#             print s
            p3 = re.compile('(\[|\]|\(|\))|\'')
            s = p3.sub('', s)
#             print s
            recom_list = s.split(':')[1].split(',')
            recom_list.pop(0)
            recom_list_all.append(recom_list[0:TopN])
    file_input.close()
    return recom_list_all

def getTargetNodes():
    with open(FILE_PATH_TARGETNODES) as file_input:
        targetNodes = file_input.readline().strip().split(',')
    return targetNodes

def getNewCoauthorList():
    targeNodes = getTargetNodes()
    mRedisHelper = RedisHelper()
    coauthorList_all = []
    for targetNode in targeNodes:
        newCoauthorList = []
        for coauthor in mRedisHelper.getCoauthors(targetNode):
            years = mRedisHelper.getCoauthorTimes(targetNode, coauthor)
            if False not in [int(year) > 2011 for year in years]:
                newCoauthorList.append(coauthor)
        coauthorList_all.append(newCoauthorList)
    return coauthorList_all

def getCoauthorList():
    targeNodes = getTargetNodes()
    mRedisHelper = RedisHelper()
    coauthorList_all = []
    for targetNode in targeNodes:
        coauthorList = []
        coauthorList = list(mRedisHelper.getCoauthors(targetNode))
        coauthorList_all.append(coauthorList)
    return coauthorList_all

if __name__ == '__main__':
    for i in range(1,41):
        RecomList = getRecomList(i*3)
#         print RecomList
        CoauthorList = getNewCoauthorList()
        countA = 0
        rec_len = 0
        coau_len = 0
        for i in range(100):
            rec_len += len(RecomList[i])
            coau_len += len(CoauthorList[i])
            for recomNode in RecomList[i]:
                for coauthor in CoauthorList[i]:
                    if recomNode == coauthor:
                        countA += 1
        precision = countA * 1.0 / rec_len
        recall = countA * 1.0 / coau_len
        print str(precision) + ' ' + str(recall) + ' ' + str(0.0 if (precision + recall) == 0 else 2.0 * precision * recall/(precision + recall))
#         print countA
#         print rec_len
#         print coau_len
#         print 'precision:' + str(precision)
#         print 'recall:' + str(recall)
#      
#         print 'F1:' + str(2.0 * precision * recall/(precision + recall))

