#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: randomwalk.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月12日 星期一 09时01分13秒
#########################################################################

import sys
sys.path.append('..')
from digraph.graph import DigraphByClass
from operator import itemgetter
from util.Params import *

def randomwalk(graph, damping_factor = 0.85, max_iterations = 100,\
        min_delta = 0.000001):
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        return {}
    rank = dict.fromkeys(nodes, 0)
    sValue = {}
    min_value = (1.0-damping_factor) / graph_size
    itertimes = 0
    for i in range(max_iterations):
        diff = 0
        for node in nodes:
            rankScore = min_value
            for referring_node in graph.incidents(node):
                rankScore += damping_factor * rank[referring_node] * \
                        getRankTo(graph, referring_node, node, sValue)
            diff += abs(rank[node] - rankScore)
            rank[node] = rankScore
        itertimes = i
        if diff < min_delta:
            break
    print '\niteration time:' + str(itertimes)
    return sorted(rank.iteritems(), key = itemgetter(1), reverse = True)


