#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: saveClasses2Words.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月08日 星期四 20时26分16秒
#########################################################################

import sys
sys.path.append("..")
from redisHelper.RedisHelper import RedisHelper

redisHelper = RedisHelper()
f = open("/home/zhenchentl/workspace/tsrecom/word2vec/classes.sorted.txt")
for line in f:
    arr = line.split(' ')
    redisHelper.addClass2Words(str(arr[0]), int(arr[1]))
