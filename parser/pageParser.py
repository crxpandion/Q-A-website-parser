#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import MySQLdb as mdb
import sys

class parsePage:
  def initDB(self):
    try:
        conn = mdb.connect(host='localhost', user='root', passwd='', db='qaparser')
    except:
        print "Error occured while connecting to the database!"

    cur = conn.cursor()

    cur.execute(" CREATE TABLE questions(qid INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(qid), "
        " statement TEXT, username VARCHAR(50), userinfo VARCHAR(100), q_datetime DATE, "
        " website VARCHAR(200) ) ENGINE=InnoDB DEFAULT CHARSET=utfpath ")

    cur.execute(" CREATE TABLE answers(aid INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(aid), "
        " qid INT, FOREIGN KEY(qid) REFERENCES questions(qid), "
        " statement TEXT, username VARCHAR(50), userinfo VARCHAR(100), a_datetime DATE) "
        " ENGINE=InnoDB DEFAULT CHARSET=utf8 ")

    #cur.execute(" CREATE TABLE comments(cid INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(cid), "
    #    " aid INT, FOREIGN KEY(aid) REFERENCES answers(aid), "
    #    " statement TEXT, username VARCHAR(50), userinfo VARCHAR(100)) "
    #    " ENGINE=InnoDB DEFAULT CHARSET=utf8 ")
    cur.close()
    conn.close()

  # insert stuff into DB
  def insertQuestion(self):
    conn = None
    try:
        conn = mdb.connect(host='localhost', user='root', passwd='', db='qaparser')
    except Exception,e:
        print e# + "Error occured while connecting to the database!"
    print self.question['question_text']
    #if self.question['question_text']:
    self.question['question_text'] = self.question['question_text'].strip('\n').replace("\'", "")
    curr = conn.cursor()
    if self.question is None:
    	self.question['user'] = 'bob'
    elif not self.question['user']:
        self.question['user'] = 'bob'
    cnt = curr.execute("INSERT INTO questions VALUES(NULL, '" + self.question['question_text'] + "', '" + self.question['user'] + "', 'something about user', NOW(), '" + self.path + "')")
    conn.commit()
    curr.execute(" SELECT qid FROM questions where statement like '" + self.question['question_text'] + "'")
    self.question['qid'] = curr.fetchone()[0]
    curr.close()
    conn.close()
  def insertAnswers(self):
    conn = None
    try:
        conn = mdb.connect(host='localhost', user='root', passwd='', db='qaparser')
    except Exception, e:
        print e#"Error occured while connecting to the database!"
    curr = conn.cursor()
    try:
        for answer in self.answers:
	    print answer
	    
    	    answer['answer'] = answer['answer'].strip('\n').replace("\'", "")
	    
	    if answer['user'] is None:
	        answer['user'] = 'bob'
	    elif not answer['user']:
	        answer['user'] = 'bob'
    	    curr.execute("INSERT INTO answers VALUES(NULL, " + str(self.question['qid']) + ",'" + answer['answer'] + "', '" + answer['user'] + "', '', NOW())")
	    conn.commit()
	    #end of for
    except Exception, e:
	print e
    curr.close()
    conn.close()

  def makeDOM(self):
    return BeautifulSoup(self.html)

  def run(self):
    try:
        self.question = self.getQuestion()
        self.answers = self.getAnswers()
        if self.verbose:
            print self.question
            print str(len(self.answers)) + ' answers found'
	print "-----------Questions---------"
        self.insertQuestion()
	print "------------Answers-----------"
        self.insertAnswers()
        return True
    except Exception, e:
        print e
        return False

  def getQuestion(self):
    raise subClassError('getQuestion is not implemented')

  def getAnswers(self):
    raise subClassError('getAnswer is not implemented')

  class subClassError(Exception):
    def __init__(self, value):
      self.value = value
    def __str__(self):
      return repr(self.value)

  def __init__(self, html, path, verbose):
    self.html = html
    self.path = path
    self.verbose = verbose
    self.dom = self.makeDOM()
