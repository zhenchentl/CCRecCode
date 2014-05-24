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
from digraph.graph import DigraphByClass
from operator import itemgetter

def getTargetNodes():
    with open(FILE_PATH_TARGETNODES) as file_input:
        targetNodes = file_input.readline().strip().split(',')
    return targetNodes

def saveRecomList(recom_dict):
    with open(FILE_PATH_RECOMLIST_CN,'a') as file_input:
        for tg in recom_dict:
            file_input.write(tg + ':' + str(recom_dict[tg]) + '\n')
        file_input.close()
# 
# def recommender(mRedisHelper, targetNode):
#     recomList = []
#     coAuthors = []
#     cocoAuthors_tmp = []
#     cocoAuthors_rank = {}
#     coAuthors_tmp = mRedisHelper.getCoauthors(targetNode)
#     for coauthor in coAuthors_tmp:
#         years = mRedisHelper.getCoauthorTimes(targetNode, coauthor)
#         if True in [int(year) <= 2011 for year in years]:
#             coAuthors.append(coauthor)
#     for coauthor in coAuthors:
#         cocos = mRedisHelper.getCoauthors(coauthor)
#         for coco in cocos:
#             coyears = mRedisHelper.getCoauthorTimes(coauthor, coco)
#             if True in [int(year) <= 2011 for year in coyears]:
#                 cocoAuthors_tmp.append(coco)
#     cocoAuthors = list(set(cocoAuthors_tmp))#包括已经合作的人
#     for cocoau in cocoAuthors:
#         cccs = []
#         cococos = mRedisHelper.getCoauthors(cocoau)
#         for ccc in cococos:
#             cccyears = mRedisHelper.getCoauthorTimes(cocoau, ccc)
#             if True in [int(year) <= 2011 for year in cccyears]:
#                 cccs.append(ccc)
#         cocoAuthors_rank[cocoau] = len(set(cccs) & set(coAuthors))
#     recomList = sorted(cocoAuthors_rank.iteritems(), key = itemgetter(1), reverse = True)[0:200]
#     return {targetNode:recomList}

def recommender():
    graph = DigraphByClass().getDigraphAll()
    targetNodes = getTargetNodes()
    index = 0
    for targetNode in targetNodes:
        index += 1
        print index
        cocoAuthors_rank = {}
        recomList = []
        coAuthors = []
        cocoAuthors = []
        coAuthors = graph.neighbors(targetNode)
        for coAuthor in coAuthors:
            cocoAuthors.extend(graph.neighbors(coAuthor))
        for coco in cocoAuthors:
            cccs = graph.neighbors(coco)
            cocoAuthors_rank[coco] = len(set(cccs) & set(coAuthors))
        recomList = sorted(cocoAuthors_rank.iteritems(), key = itemgetter(1), reverse = True)[0:200]
        saveRecomList({targetNode:recomList})

if __name__ == '__main__':
    recommender()
#     mRedisHelper = RedisHelper()
#     index = 0
#     for targetNode in getTargetNodes():
#         index += 1
#         print index
#         recom_dict = recommender(mRedisHelper, targetNode)
#         saveRecomList(recom_dict)
#     #print getTargetNodes()
