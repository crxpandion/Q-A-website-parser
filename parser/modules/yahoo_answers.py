#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage 

class parseQAPage(parsePage):
    def getQuestion(self):
        q = {}
        question_field = self.dom.find('div', id='yan-question')
        title = str((question_field.find('h1', 'subject').contents[0].lstrip().rstrip()))
        questionLong = str(question_field.find('div', 'content').contents).lstrip().rstrip()
        datetime = question_field.find('abbr')['title'].split(' ')
        q['question_text'] = title + ' ' + questionLong
        q['datetime'] = datetime[0] + ' ' + datetime[1]
        q['user'] = question_field.find('span', 'user').find('span', 'fn')['title']
        return q

    def getAnswers(self):
        answers = self.dom.findAll( 'div', 'answer')
        a = []
        for answer in answers:
            ans = {}
            datetime = answer.find('abbr')['title'].split(' ')
            ans['datetime'] = datetime[0] + ' ' + datetime[1]
            ans['answer'] = str(answer.find('div', 'content').contents)
            if answer.find('div', 'vote-count'):
                ans['upVotes'] = answer.find('div', 'vote-count').find('span').contents[0]
            else:
                ans['upVotes'] = 0
            ans['user'] = answer.find('span', 'user').find('span', 'fn')['title']
            a.append(ans)
        return a
