#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: saveCoauthorShip.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月08日 星期四 20时22分07秒
#########################################################################

from redisHelper.RedisHelper import RedisHelper

def saveCoauthorShip(authors,year):
    redisHelper = RedisHelper()
    if len(authors) > 1:
        for au in authors:
            for coau in authors:
                if au != coau:
                    try:
                        redisHelper.addCoauthorship(au, coau, year)
                    except:
                        print 'add error: ' + str(au) + '==' + str(coau)
