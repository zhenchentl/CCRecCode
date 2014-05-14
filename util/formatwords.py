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
    p = re.compile('(and |for |of |this |there |those |then |too |we |what |how \
            |when |which |why |who |was |is |yes |no |by |she |he |her |to |from \
            |than |in |a |an |or |they |them |their |his |him |where |the |whom \
            |not |may |might |us |me |our |my |own |whose |well |will |do |are \
            |was |be |were |you |your |but |however |more |much |most )')
    s = p.sub(' ', s)
    return s

f = open("/home/zhenchentl/workspace/tsrecom/dblp/segmentwords_all.txt")
formatedWords = ''
for line in f:
    s = formatwords(line)
    formatedWords += s
f.close()
f2 = open("/home/zhenchentl/workspace/tsrecom/dblp/segmentwords_all_formated.txt",'w+')
f2.write(formatedWords)
f2.close()
formatedWords = ''
s = ''
