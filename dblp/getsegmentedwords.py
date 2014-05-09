#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2014-04-26
Description:对data mining的dblp数据进行分词，获取语料
@author: zhenchentl
'''
from xml.sax import handler, make_parser
import time

DBLP_XML_PATH = '/home/zhenchentl/dblp/dblp.xml'

paperTag = ('article','inproceedings','proceedings','book',
        'incollection','phdthesis','mastersthesis','www')

IOTIMEFORMAT = '%Y-%m-%d %X'

class dblpHandler(handler.ContentHandler):
    
    def __init__(self):
        self.isPaperTag = False
        self.isTitleTag = False
        self.segmentdWords = ''
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
#             self.isPaperTag = True
            confName = attrs.get('key').split('/')[1]
            if confName in self.confList:
                self.isPaperTag = True
        if name == 'title' and self.isPaperTag:
            self.isTitleTag = True
            self.count += 1
    
    def endElement(self, name):
        if name in paperTag:
            if self.isPaperTag:
                self.isPaperTag = False
    
    def characters(self, content):
        if self.isTitleTag:
            self.segmentdWords += content
            self.segmentdWords += ' '
            self.isTitleTag = False
            if self.count%100 == 0:
                #每读取10000个文章标题，就保存一次
                saveSegmentedWords(self.segmentdWords)
                self.segmentdWords = ''
                if self.count%10000 == 0:
                    print self.count

def saveSegmentedWords(segmentdWords):
#     try:
    file_output = open('/home/zhenchentl/dblp/segmentwords.txt', 'a')
    file_output.write(segmentdWords)
    file_output.close()
#     except:
#         print 'write title error!'

def getConfList():
    file_input = open('/home/zhenchentl/dblp/conflist.txt')
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
