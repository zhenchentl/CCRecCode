#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: getSomeTargetNode.py
# Author: Mark Chen
# mail: zhenchentl@gmail.com
# Created Time: 2014年05月12日 星期一 20时21分36秒
#########################################################################

import sys
sys.path.append('..')

from redisHelper.RedisHelper import RedisHelper
from util.Params import *
import random
def getSomeTargetNode(num = 100, min_degree = 30):
    with open(FILE_PATH_TARGETNODES, 'w') as file_input:
        mRedisHelper = RedisHelper()
        authors = mRedisHelper.getAuthors()
        num = 0
        while True:
            author = random.choice(authors)
            CoLen = len(list(mRedisHelper.getCoauthors(author)))
            if CoLen > min_degree:
                file_input.write(author + ',')
                num += 1
                if num >= 100:
                    break
        file_input.close()
if __name__ == '__main__':
    getSomeTargetNode(TargetNodesNum, TargetNodesMinDegree)
