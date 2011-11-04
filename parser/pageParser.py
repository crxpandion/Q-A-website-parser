#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup

class parsePage:
  class subClassError(Exception):
    def __init__(self, value):
      self.value = value
    def __str__(self):
      return repr(self.value)

  def __init__(self, url):
    self.url = url
    self.dom = self.makeDOM()

  def makeDOM(self):
    return BeautifulSoup(urllib2.urlopen(self.url).read())
  
  def run(self):
    try:
        self.question = self.getQuestion()
        self.answers = self.getAnswers()
        self.insertQuestion()
        self.insertAnswers()
        return True
    except:
        #raise Error Error('Error in Run')
        print 'scraping or inserting failed...'
        return False

  # insert stuff into DB 
  def insertQuestion(self):
    print 'insertQuestion is not implemented yet'

  def insertAnswers(self):
    print 'insertAnswers is not implemented yet'

  # these will be overloaded in the modules 
  def getQuestion(self):
    raise subClassError('getQuestion is not implemented')

  def getAnswer(self):
    raise subClassError('getAnswer is not implemented')

