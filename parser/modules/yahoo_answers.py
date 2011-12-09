#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage 

class parseQAPage(parsePage):
    def getQuestion(self):
        q = {}
        question_field = self.dom.find('div', id='yan-question')
        try:
            title = str((question_field.find('h1', 'subject').contents[0].lstrip().rstrip()))
            questionLong = str(question_field.find('div', 'content').contents).lstrip().rstrip()
            q['question_text'] = title + ' ' + questionLong
        except:
            q['question_text'] = 'NA'
        try:    
            datetime = question_field.find('abbr')['title'].split(' ')
            q['datetime'] = datetime[0] + ' ' + datetime[1]
        except:
            q['datetime'] = 'NA'
        try:
            q['user'] = question_field.find('span', 'user').find('span', 'fn')['title']
        except:
            q['user'] = 'NA'
        return q

    def getAnswers(self):
        answers = self.dom.findAll( 'div', 'answer')
        a = []
        for answer in answers:
            ans = {}
            try:
                datetime = answer.find('abbr')['title'].split(' ')
                ans['datetime'] = datetime[0] + ' ' + datetime[1]
            except:
                ans['datetime'] = 'NA'
            try:
                ans['answer'] = unicode(answer.find('div', 'content').contents)
            except:
                ans['answer'] = 'NA'
            try:
                if answer.find('div', 'vote-count'):
                    ans['upVotes'] = answer.find('div', 'vote-count').find('span').contents[0]
                else:
                    ans['upVotes'] = 0
            except:
                ans['upVotes'] = 'NA'
            try:
                ans['user'] = unicode(answer.find('span', 'user').find('span', 'fn')['title'])
            except:
                ans['user'] = 'NA'
            a.append(ans)
        return a
