#!/usr/bin/python
from bs4 import BeautifulSoup
from ..pageParser import parsePage 

class parseQAPage(parsePage):
  def getQuestion(self):
    question_field = self.dom.find('div', id='yan-question')
    question_title = question_field.fint('h1', 'subject')
    question_test = question_field.find('div', 'content')
    print question_test
    print question_title

  def getAnswer(self):
    print 'not implemented yet'

# small tests - we should really get a testing package going...
pp = parseQAPage('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS')
pp.getQuestion()
