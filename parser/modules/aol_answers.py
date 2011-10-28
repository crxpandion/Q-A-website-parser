#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage 

class parseQAPage(parsePage):
    def getQuestion(self):
      q = {}
      user = {}
      question_field = self.dom.find('div', id='QuestionBlogPostDetails')
      content = question_field.find('div', 'Content')
      # user['name']
      # user['stats']
      q['time'] = question_field.find('span', 'PostedOn')
      q['title'] = ''
      q['question'] = content.find('h1')
      q['user'] = content.find('a', attrs={'title':True})
      return q

    def getAnswer(self):
      answers = self.dom.findAll( 'div', 'AnswersSectionContentInner')
      a = []
      for answer in answers:
          user = {}
          ans = {}
          ans['time'] = answer.find('a', 'PostedOn')
          ans['content'] = answer.find('p')
          ans['rating'] = answer.find('span', 'QBRankVoteHeader')
          user['name'] = answer.find('a', attrs={'title':True})
          # user['stats']
          ans['user'] = user
          a.append(ans)
      return a

# small tests - we should really get a testing package going...
#Anonymous
#pp = parseQAPage('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250')
#Not Anonymous
#pp = parseQAPage('http://aolanswers.com/questions/politics_government_627011121388373')
#lots of answers
pp = parseQAPage('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250')

pp.getQuestion()
pp.getAnswer()
