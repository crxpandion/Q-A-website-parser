#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage
import datetime

class parseQAPage(parsePage):
    def getQuestion(self):
        q = {}
        question_field = self.dom.find('div', id='qnaQuesComm')
        q['question_text'] = question_field.find('div', 'txt_xxlg abstract pl15 pb10').contents[0].lstrip().rstrip()
        q['user'] = question_field.find('div', 'rr_life_title b').contents[0].replace(' asked','')
        q['datetime'] = 'not_given'
        return q
        
    def getAnswers(self):
        a = []
        answers = self.dom.findAll('div', 'ansbrd')[1:]
        for answer in answers:
            ans = {}
            info = answer.findAll('span')
            ans['user'] = info[0].string.replace(':', '')
            ans['answer'] = info[1].string
            ans['datetime'] = getPostDate(answer.find('div', 'clrg pt10').string)
            ans['upVotes'] =  answer.find('div', 'fl pr15 ml5').string
            a.append(ans)
        return a
		
def getPostDate(postedOn):
    if 'year' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[1]) * 365)).split()[0] + ' 00:00:00'        
    elif 'month' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[1]) * 30.5)).split()[0] + ' 00:00:00'
    elif 'day' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[1]))).split()[0] + ' 00:00:00'
    else:
        return str(datetime.datetime.now())
