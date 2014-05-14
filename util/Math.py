#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: Math.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月12日 星期一 19时31分35秒
#########################################################################
from math import sqrt

'''余弦相似度'''
def sim_distance_cos(p1, p2):
    '''p1和p2是dict的话，遍历会更迅速'''
    c = min(len(p1), len(p2))
    ss = sum([float(p1[i]) * float(p2[i]) for i in xrange(c)])
    sq1 = sqrt(sum([pow(float(p1[i]), 2) for i in p1]))
    sq2 = sqrt(sum([pow(float(p2[i]), 2) for i in p2]))
    if sq1 * sq2 != 0:
        return float(ss)/(sq1 * sq2)
    return 0.0

'''得到topN相似度高的学者'''
#def topMatches()
