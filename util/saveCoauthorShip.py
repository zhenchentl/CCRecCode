#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: saveCoauthorShip.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月08日 星期四 20时22分07秒
#########################################################################

import redisHelper.RedisHelper import RedisHelper

def saveCoauthorShip(authors):
    redisHelper = RedisHelper()
    if len(authors) > 1:
        for au in authors:
            for coau in authors:
                if au != coau:
                    redisHelper.addcoauhtorship(au, coau)
