#!/usr/bin/python
import urllib2
import yahoo_answers
import aol_answers
import askville_answers
import ask_answers
import unittest
import datetime

class checkScrape(unittest.TestCase):
    def __init__(self, url, question, answer):
        self.url = url
        self.question = question
        self.answer = answer
        self.runTest()
        
    def runTest(self):
        if 'http://aolanswers.com' in self.url:
            self.checkQuestionAndAnswer(aol_answers.parseQAPage(urllib2.urlopen(self.url).read(), '', False))
        if 'http://answers.yahoo.com' in self.url:
            self.checkQuestionAndAnswer(yahoo_answers.parseQAPage(urllib2.urlopen(self.url).read(), '', False))
        if 'http://answers.ask.com/' in self.url:
     	    self.checkQuestionAndAnswer(ask_answers.parseQAPage(urllib2.urlopen(self.url).read(), '', False))
     	if 'http://askville.amazon.com/' in self.url:
     	    self.checkQuestionAndAnswer(askville_answers.parseQAPage(urllib2.urlopen(self.url).read(), '', False))

    def checkQuestionAndAnswer(self, p):
        self.checkQuestion(p.getQuestion())
     	self.checkAnswer(p.getAnswers()[0])
	p.run()
            
    def checkQuestion(self, question):
        assert question['question_text'] == self.question['question_text'], 'Question text did not match'
        assert dateWithinOneDay(question['datetime'], self.question['datetime']), 'Datetime did not match ' + self.question['datetime'] + ' ' + question['datetime']
        assert question['user'] == self.question['user'], 'User did not match'

    def checkAnswer(self, answer):
        assert answer['answer'] == self.answer['answer'], 'Answer text did not match'
        assert answer['upVotes'] == self.answer['upVotes'], 'UpVotes did not match'
        assert dateWithinOneDay(answer['datetime'], self.answer['datetime']), 'Datetime did not match ' + self.answer['datetime'] + ' ' + answer['datetime']

def dateWithinOneDay(answer, scraped):
    time_format = "%Y-%m-%d %H:%M:%S"
    answer = datetime.datetime.strptime(answer, time_format)
    scraped = datetime.datetime.strptime(scraped, time_format)
    return abs((answer - scraped).days) < 2


#Example:
# AOL - no user
question = {'question_text': 'Are the poor people better off today rather than four years ago?', \
            'user': None, \
            'datetime': '2011-11-06 00:00:00'}
answer = {'answer': 'I think in general, you have a few marbles loose upstairs.....You must of been dong some heavy relaps in drugs, or slept for all those years.....Good, Mr. Van Winkle...', \
          'upVotes': '0', \
          'datetime': '2011-11-06 00:00:00'}
checkScrape('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250', question, answer)

print 'All Tests Passed'
