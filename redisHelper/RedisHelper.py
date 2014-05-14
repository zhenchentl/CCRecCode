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
DB_AUTHORS_RANK_VEC = 5
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
        '''key-->list:存储学者的特征向量。author-->[rank,rank,rank...]'''
        self.authorsRankVec = redis.StrictRedis('127.0.0.1', port = 6379, \
                db = DB_AUTHORS_RANK_VEC)
    def addClass2Words(self, word, classID):
        '''添加classID和单词的键值对'''
        return self.wordClassesDB.set(word, classID)

    def addCoauthorship(self, author, coauthor):
        '''添加论文合作关系key-->set'''
        return self.coauthorShipDB.sadd(author, coauthor)

    def addClassifyItem(self, author, classID):
        '''增加一条学者分类信息'''
        if self.classAuthorsDB.sadd(classID, author) == 1:
            pass
        else:
            num = self.classAuthorNumDB.get(str(classID) + ':' + author)
            if num != None:
                self.classAuthorNumDB.set(str(classID) + ':' + author, int(num) + 1)
            else:
                self.classAuthorNumDB.set(str(classID) + ':' + author, 2)
        self.authorClassesDB.sadd(author, classID)

    def addAuthorScore(self, author, score):
        '''添加学者的某rank值'''
        self.authorsRankVec.lpush(author, score)

    def getClassIDbyWord(self, word):
        '''根据单词获取ClassID'''
        return self.wordClassesDB.get(word)

    def getAuthorsByClassID(self, classID):
        '''根据classID获取作者列表'''
        return self.classAuthorsDB.smembers(classID)

    def getAuthorWordsNumInClass(self, classID, author):
        '''根据作者名和类ID获取此作者在该类中的单词数'''
        return self.classAuthorNumDB.get(str(classID) + ':' + author)

    def getCoauthors(self, author):
        '''根据作者名获取合作者列表'''
        return self.coauthorShipDB.smembers(author)

    def getClassIDs(self):
        '''获取所有的classID'''
        return self.classAuthorsDB.keys()

    def getAuthors(self):
        '''获取所有的作者'''
        return self.authorClassesDB.keys()

    def getAuthorVec(self, author):
        '''获取作者的特征向量'''
        return self.authorsRankVec.lrange(author, 0, -1)
