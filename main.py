#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: main.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月12日 星期一 20时15分49秒
#########################################################################
import sys
sys.path.append('..')
from util.Params import *
from util.Math import *
from redisHelper.RedisHelper import RedisHelper
from operator import itemgetter

def getTargetNodes():
    with open(FILE_PATH_TARGETNODES) as file_input:
        targetNodes = file_input.readline().strip().split(',')
    return targetNodes

def saveRecomList(recom_dict):
    with open(FILE_PATH_RECOMLIST,'a') as file_input:
        for tg in recom_dict:
            file_input.write(tg + ':' + str(recom_dict[tg]) + '\n')
        file_input.close()

def recommender(mRedisHelper, targetNode):
    tgNodeVec_li = list(mRedisHelper.getAuthorVec(targetNode))
    tgNodeVec_dict = dict(zip(range(len(tgNodeVec_li)), tgNodeVec_li))
    nodes = mRedisHelper.getAuthors()
    recommendedNodes = {}
    recom_dict = {}
    index = 0
    for node in nodes:
        index += 1
        if index % 1000 == 0:
            print index
        nodeVec_li = list(mRedisHelper.getAuthorVec(node))
        nodeVec_dict = dict(zip(range(len(nodeVec_li)), nodeVec_li))
        recommendedNodes[node] = sim_distance_cos(tgNodeVec_dict, nodeVec_dict)
    print 'all sim caculate done!'
    TopNRecommendedNode = sorted(recommendedNodes.iteritems(), key = itemgetter(1), \
            reverse = True)[0 : RecomTopN]
    recom_dict[targetNode] = TopNRecommendedNode
    recommendedNodes = {}
    return recom_dict
if __name__ == '__main__':
    mRedisHelper = RedisHelper()
    for targetNode in getTargetNodes():
        recom_dict = recommender(mRedisHelper, targetNode)
        saveRecomList(recom_dict)
    #print getTargetNodes()
