#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: getrankscoreofauthors.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月12日 星期一 15时57分06秒
#########################################################################

import sys
sys.path.append('..')

from randomwalk.randomwalk import randomwalk
from redisHelper.RedisHelper import RedisHelper
from digraph.graph import DigraphByClass

def getrankscoreofauthors():
    mRedisHelper = RedisHelper()
    classIDs = mRedisHelper.getClassIDs()
    index = 0
    for classID in classIDs:
        graph = DigraphByClass().getDigraph(classID)
        ranks = randomwalk(graph)
        for author, rankscore in ranks:
            mRedisHelper.addAuthorScore(author, rankscore)
        authors_all = mRedisHelper.getAuthors()
        authors_class = dict(ranks).keys()
        authors_diff = list(set(authors_all).difference(set(authors_class)))
        for au_diff in authors_diff:
            mRedisHelper.addAuthorScore(au_diff, 0)
        index += 1
        print index
if __name__ == '__main__':
    getrankscoreofauthors()
