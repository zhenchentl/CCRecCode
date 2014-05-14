#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: graph.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月12日 星期一 09时11分35秒
#########################################################################
import sys
sys.path.append("..")
from redisHelper.RedisHelper import RedisHelper
from pygraph.classes.digraph import digraph

class DigraphByClass:
    def __init__(self):
        self.mDigraph = digraph()
        self.mRDHelper = RedisHelper()

    def getDigraph(self, classID):
        authors = self.mRDHelper.getAuthorsByClassID(classID)
        for author in authors:
            if not self.mDigraph.has_node(author):
                nValue = self.mRDHelper.getAuthorWordsNumInClass(classID, author)
                self.mDigraph.add_node(author, ('value',nValue))
        for author in authors:
            coAuthors = self.mRDHelper.getCoauthors(author)
            for coauthor in coAuthors:
                if self.mDigraph.has_node(coauthor) and \
                        not self.mDigraph.has_edge((author, coauthor)):
                    self.mDigraph.add_edge((author, coauthor))
            coAuthors = []
        authors = []
        return self.mDigraph
