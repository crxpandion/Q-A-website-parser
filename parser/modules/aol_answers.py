#!/usr/bin/python
import sys, urllib2, re
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage
import datetime

class parseQAPage(parsePage):
    def getQuestion(self):
        q = {}
        question_field = self.dom.find('div', id='QuestionBlogPostDetails')
        content = question_field.find('div', 'Content')
        try:
            tag = question_field.find('span', 'PostedOn')
            if len(tag) > 1:
                q['datetime'] = getPostDate(tag.contents[-1].string)
            else:
                q['datetime'] = getPostDate(tag.contents[-1].string)
        except:
            q['datetime'] = 'NA'
        try:
            q['question_text'] = str(content.find('h1').contents[0].lstrip().rstrip())
        except:
            q['question_text'] = 'NA'
        try:
            q['user'] = str(content.find('a', attrs={'title':True}).string)
        except:
            q['user'] = 'NA'
        return q

    def getAnswers(self):
        answers = self.dom.findAll( 'div', 'AnswersSectionContentInner')
        a = []
        for answer in answers:
            ans = {}
            try:
                ans['datetime'] = getPostDate(answer.find('a', 'PostedOn').string)
            except:
                ans['datetime'] = 'NA'
            try:
                ans['answer'] = str(answer.find('p').string)
            except:
                ans['answer'] = 'NA'
            try:
                ans['upVotes'] = str(answer.find('span', 'QBRankVoteHeader').contents[0][1])
            except:
                ans['upVotes'] = 'NA'
            try:
                user = answer.find('a', attrs={'title':True})
                ans['user'] = 'None'
                if user:
                    ans['user'] = str(answer.find('a', attrs={'title':True})['title'])
            except:
                ans['user'] = 'NA'
            a.append(ans)
        return a
    
def getPostDate(postedOn):
    num = 0
    for item in str(postedOn).split():
        if item.isdigit():
            num = int(item)
    if 'year' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(num) * 365)).split()[0] + ' 00:00:00'        
    elif 'month' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(num) * 30.5)).split()[0] + ' 00:00:00'
    elif 'day' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(num))).split()[0] + ' 00:00:00'
    else:
        return str(datetime.datetime.now())
