#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage 

class parseQAPage(parsePage):
  def getQuestion(self):
    q = {}
    user = {}
    question_field = self.dom.find('div', id='yan-question')
    q['title'] = question_field.find('h1', 'subject')
    q['question'] = question_field.find('div', 'content')
    # user['name']
    # user['stats']
    q['user'] = user
    return q

  def getAnswer(self):
    answers = self.dom.findAll( 'div', 'answer')
    a = []
    for answer in answers:
        user = {}
        ans = {}
        ans['time'] = answer.find('abbr')
        ans['content'] = answer.find('div', 'content')
        ans['rating'] = answer.find('span', 'seo-rated')
        # user['name']
        # user['stats']
        ans['user'] = user
        a.append(ans)
    return a


# small tests - we should really get a testing package going...
pp = parseQAPage('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS')
pp.getQuestion()
pp.getAnswer()
