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
    self.question = self.getQuestion()
    self.answer = self.getAnswer()
    self.insertQuestion()
    self.insertAnswer()

  # insert stuff into DB 
  def insertQuestion(self):
    print 'insertQuestion is not implemented yet'

  def insertAnswer(self):
    print 'insertAnswer is not implemented yet'

  # these will be overloaded in the modules 
  def getQuestion(self):
    raise subClassError('getQuestion is not implemented')

  def getAnswer(self):
    raise subClassError('getAnswer is not implemented')
