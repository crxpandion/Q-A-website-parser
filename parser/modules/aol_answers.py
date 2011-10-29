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
        q['datetime'] = question_field.find('span', 'PostedOn').string
        q['question_text'] = content.find('h1').contents[0].lstrip().rstrip()
        q['user'] = content.find('a', attrs={'title':True})
        return q

    def getAnswers(self):
        answers = self.dom.findAll( 'div', 'AnswersSectionContentInner')
        a = []
        for answer in answers:
            user = {}
            ans = {}
            ans['datetime'] = answer.find('a', 'PostedOn')
            ans['answer'] = answer.find('p')
            ans['upVotes'] = answer.find('span', 'QBRankVoteHeader')
            user['user'] = answer.find('a', attrs={'title':True})
            a.append(ans)
        return a
