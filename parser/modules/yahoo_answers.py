#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage 

class parseQAPage(parsePage):
  def getQuestion(self):
    question_field = self.dom.find('div', id='yan-question')
    title = question_field.find('h1', 'subject')
    question = question_field.find('div', 'content')
    #insertQuestion(...)

  def getAnswer(self):
    answers = self.dom.findAll( 'div', 'answer')
    for answer in answers:
        time = answer.find('abbr')
        content = answer.find('div', 'content')
        rating = answer.find('span', 'seo-rated')
        #insertAnswer(...)

# small tests - we should really get a testing package going...
pp = parseQAPage('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS')
pp.getQuestion()
pp.getAnswer()
