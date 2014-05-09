#!/usr/bin/env python
#coding=utf-8
#########################################################################
# File Name: RedisHelper.py
# Author: Lisa & Mark Chen
# Mail: zhenchentl@gmail.com
# Created Time: 2014年05月04日 星期日 15时09分20秒
#########################################################################

import redis

DB_WORDS_CLASSES = 0
DB_COAUTHORSHIP = 1
DB_CLASS_AUTHORS = 2
DB_AUTHOR_CLASSES = 3
DB_CLASS_AUTHOR_NUM = 4
class RedisHelper:

    def __init__(self):
        '''key-->value:存储关键词类别。keywords-->classID'''
        self.wordClassesDB = redis.StrictRedis('127.0.0.1', port = 6379, \
                db = DB_WORDS_CLASSES)
        '''key-->set:存储论文合作者关系。authorname-->coauthorName'''
        self.coauthorShipDB = redis.StrictRedis('127.0.0.1', port = 6379, \
                db = DB_COAUTHORSHIP)
        '''key-->set:存储每类中的学者。classID-->author'''
        self.classAuthorsDB = redis.StrictRedis('127.0.0.1', port = 6379, \
                db = DB_CLASS_AUTHORS)
        '''key-->set:存储学者都属于哪些类。author-->classID'''
        self.authorClassesDB = redis.StrictRedis('127.0.0.1', port = 6379, \
                db = DB_AUTHOR_CLASSES)
        '''key-->value:存储学者在某类中关键词数目。classID:author-->num'''
        self.classAuthorNumDB = redis.StrictRedis('127.0.0.1', port = 6379, \
                db = DB_CLASS_AUTHOR_NUM)
    def addClass2Words(self, word, classID):
        return self.wordClassesDB.set(word, classID)

    def addCoauthorship(self. author, coauthor):
        return self.coauthorShipDB.sadd(author, coauthor)

    def addclassifyItem(self, author, classID):
        if self.classAuthorsDB.sadd(classID, author) == 1:
            pass
        else:
            num = self.classAuthorNumDB.get(classID + ':' + author)
            if num != None:
                self.classAuthorNumDB.set(classID + ':' + author, num + 1)
            else:
                self.classAuthorNumDB.set(classID + ':' + author, 2)
        self.authorClassesDB.sadd(author, classID)

    def getClassIDbyWord(self, word):
        return self.wordClassesDB.get(word)

