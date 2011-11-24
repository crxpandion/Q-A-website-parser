#!/usr/bin/python
import sys, urllib2
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage 
import datetime

class parseQAPage(parsePage):
    def getQuestion(self):
        q = {}
        question_field = self.dom.find('div', id='QuestionBlogPostDetails')
        content = question_field.find('div', 'Content')
        q['datetime'] = getPostDate(question_field.find('span', 'PostedOn').string)
        q['question_text'] = content.find('h1').contents[0].lstrip().rstrip()
        q['user'] = content.find('a', attrs={'title':True})
        return q

    def getAnswers(self):
        answers = self.dom.findAll( 'div', 'AnswersSectionContentInner')
        a = []
        for answer in answers:
            ans = {}
            ans['datetime'] = getPostDate(answer.find('a', 'PostedOn').string)
            ans['answer'] = answer.find('p').string
            ans['upVotes'] = answer.find('span', 'QBRankVoteHeader').contents[0][1]
            user = answer.find('a', attrs={'title':True})
            ans['user'] = 'None'
            if user:
                ans['user'] = answer.find('a', attrs={'title':True})['title']
            a.append(ans)
        return a

def getPostDate(postedOn):
    return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[1]))).split()[0] + ' 00:00:00'
