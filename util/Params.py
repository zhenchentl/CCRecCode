#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: Params.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月12日 星期一 19时45分29秒
#########################################################################

from pygraph.classes.digraph import digraph

RecomTopN = 200

ReconListSize= 30

TargetNodesMinDegree = 30

TargetNodesNum = 100

FILE_DIR = '/home/zhenchentl/workspace/tsrecom/'

RECOM_LIST_PATH = FILE_DIR + 'recom_list_14.txt'

DBLP_XML_PATH = FILE_DIR + 'dblp/dblp.xml'

FILE_OUTPUT_PATH_SEGMENTWORDS = FILE_DIR + 'dblp/segmentwords.txt'

FILE_INPUT_PATH_CONFLIST = FILE_DIR + 'dblp/conflist.txt'

FILE_PATH_TARGETNODES = FILE_DIR + 'dblp/targetnodes.txt'

FILE_PATH_RECOMLIST = FILE_DIR + 'recom_list.txt'

def getRankTo(gra, from_node, to_node, s):
    if s.has_key(from_node + ':' + to_node):
        return s[from_node + ':' + to_node]
    #total_wt = 0.0
    #for tmp_node in gra.neighbors(from_node):
    #    total_wt = total_wt + gra.edge_weight((from_node, tmp_node))
    #S[from_node + ':' + to_node] = var \
    #        = gra.edge_weight((from_node, to_node)) / total_wt
    s[from_node + ':' + to_node] = var = 1.0 / len(gra.neighbors(from_node))
    return var
