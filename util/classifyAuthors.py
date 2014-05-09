#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: classifyAuthors.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月08日 星期四 20时16分12秒
#########################################################################

import redisHelper.RedisHelper import RedisHelper

def classifyAuthors(authors, title):
    redisHelper = RedisHelper()
    for word in title:
        classID = redisHelper.getClassIDbyWord(word)
        if classID != None:
            for au in authors:
                redisHelper.addClassifyItem(au, classID)
