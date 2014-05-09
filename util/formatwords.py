#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: formatwords.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月04日 星期日 21时18分20秒
#########################################################################

import re

def formatwords(s):
    '''格式化所有单词，去掉无用符号，去掉无意义单词，转换为小写'''
    s = re.sub("[^a-zA-Z0-9\-]", " ", s)
    s = s.lower()
    s = s.replace("and" and "for" and "of" and "this" and "there" and "those" and \
            "then" and "too" and "we" and "what" and "how" and "when" and "which" and \
            "why" and "who" and "was" and "is" and "yes" and "no" and "by" and "she" and \
            "he" and "her" and "to" and "from" and "than" and "in" and "a" and "an" and \
            "or" and "they" and "them" and "their" and "his" and "him" and "where" and \
            "the" and "whom" and "not" and "may" and "might" and "us" and "me" and \
            "our" and "my" and "own" and "whose" and "well" and "will" and "do" and \
            "are" and "was" and "be" and "were" and "you" and "your" and "but" and \
            "however" and "more" and "much" and "most", " ")
    return s

f = open("/home/zhenchentl/workspace/tsrecom/dblp/segmentwords_DM.txt")
formatedWords = ''
for line in f:
    s = formatwords(line)
    formatedWords += s
f.close()
f2 = open("/home/zhenchentl/workspace/tsrecom/dblp/segmentwords_DM_formated.txt",'w+')
f2.write(formatedWords)
f2.close()
formatedWords = ''
s = ''
