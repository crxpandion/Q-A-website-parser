#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage
import datetime

class parseQAPage(parsePage):
    def getQuestion(self):
        q = {}
        question_field = self.dom.find('div', 'question_outer')
        title = question_field.find('h1', id='question_summary').find(id='question_link').contents[0].lstrip().rstrip()
        questionLong = question_field.find('div', id='question_details').contents[0].rstrip().lstrip()
        user = question_field.find('a', 'mininav').contents[0].lstrip().rstrip()
        datetime = question_field.find('span', 'byline')['title'].split(' ')
        q['question_text'] = title + ": " + questionLong
        q['user'] = user
        q['datetime'] = datetime[0] + ' ' + datetime[1] + ':00'
        return q

    def getAnswers(self):
        a = []
        answers = self.dom.findAll('div', 'answer_outer')
        upVotes = self.dom.findAll('div', 'top_vote_bar')
        for answer in answers:
            ans = {}
            idNum = answer.find('h2', 'answer_summary')
            if idNum:
                idNum = 'votes_' + str(idNum['id'].replace('answer_summary_', ''))
                ans['upVotes'] = '0'
                for item in upVotes:
                    if str(idNum) == str(item['id']) and item.find('span'):
                        ans['upVotes'] = item.find('span').string.rstrip()
                        break
                ans['answer'] = answer.find('h2', 'answer_summary').string + unicode(answer.find('div', 'mywrite_content')).replace('<!--  mywrite content -->', '')
                ans['datetime'] = getPostDate(answer.find('div', 'byline').contents[2].rstrip().lstrip())
                ans['user'] = answer.find('div', 'byline').find('a', 'mininav').string.rstrip().lstrip()        
                a.append(ans)
        return a
        
def getPostDate(postedOn):
    if 'year' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[0]) * 365)).split()[0] + ' 00:00:00'        
    elif 'month' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[0]) * 30.5)).split()[0] + ' 00:00:00'
    elif 'day' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[0]))).split()[0] + ' 00:00:00'
    else:
        return str(datetime.datetime.now())
        
parseQAPage('http://askville.amazon.com/long-sun-Vitamin-day/AnswerViewer.do?requestId=76403763').getAnswers()
parseQAPage('http://askville.amazon.com/sheryl-crow-version-song-sun/AnswerViewer.do?requestId=8804279').getAnswers()
parseQAPage('http://askville.amazon.com/formation-sun-dog/AnswerViewer.do?requestId=5657915').getAnswers()
parseQAPage('http://askville.amazon.com/Universe-expanding-result-Big-Bang-collapse-start/AnswerViewer.do?requestId=74787617').getAnswers()
