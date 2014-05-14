#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2014-04-26
Description:对data mining的dblp数据进行分词，获取语料
@author: zhenchentl
'''
import sys
sys.path.append("..")
from xml.sax import handler, make_parser
from redisHelper.RedisHelper import RedisHelper
from util.classifyAuthors import classifyAuthors
from util.saveCoauthorShip import saveCoauthorShip
from util.formatwords import formatwords
import time

paperTag = ('article','inproceedings','proceedings','book',
        'incollection','phdthesis','mastersthesis','www')

IOTIMEFORMAT = '%Y-%m-%d %X'
isDataMining = True

class dblpHandler(handler.ContentHandler):
    
    def __init__(self):
        self.isPaperTag = False
        self.isTitleTag = False
        self.isAuthor = False
        self.authors = []
        self.title = ''
        self.count = 0
        self.confList = getConfList()
        print self.confList
    
    def startDocument(self):
        print 'Document Start time:' \
            + time.strftime(IOTIMEFORMAT, time.localtime())
    
    def endDocument(self):
        print 'count all:' + str(self.count)
        print 'Document End time:' \
            + time.strftime(IOTIMEFORMAT, time.localtime())
    
    def startElement(self, name, attrs):
        if name in paperTag:
            if isDataMining:
                confName = attrs.get('key').split('/')[1]
                if confName in self.confList:
                    self.isPaperTag = True
            else:
                self.isPaperTag = True
        if name == 'title' and self.isPaperTag:
            self.isTitleTag = True
            self.count += 1
            if self.count%1000 == 0:
                print self.count
        if name == 'author' and self.isPaperTag:
            self.isAuthor = True
    
    def endElement(self, name):
        if name in paperTag:
            if self.isPaperTag:
                self.isPaperTag = False
                classifyAuthors(self.authors, self.title)
                saveCoauthorShip(self.authors)
                self.authors = []
                self.title = ''
    
    def characters(self, content):
        if self.isTitleTag:
            self.title = formatwords(content)
            self.isTitleTag = False
        if self.isAuthor:
            self.authors.append(content)
            self.isAuthor = False

def getConfList():
    file_input = open(FILE_INPUT_PATH_CONFLIST)
    ConfList = file_input.readline().strip().split(',')
    file_input.close()
    return ConfList

def parserDblpXml():
    handler = dblpHandler()
    parser = make_parser()
    parser.setContentHandler(handler)
    f = open(DBLP_XML_PATH, 'r')
    parser.parse(f)
    f.close()

if __name__ == '__main__':
    parserDblpXml()
