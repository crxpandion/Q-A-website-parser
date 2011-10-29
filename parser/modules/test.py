#!/usr/bin/python
import yahoo_answers
import aol_answers
import unittest

class checkScrape(unittest.TestCase):
    def __init__(self, url, question, answer):
        self.url = url
        self.question = question
        self.answer = answer
        self.runTest()
        
    def runTest(self):
        if 'http://aolanswers.com' in self.url:
            p = aol_answers.parseQAPage(self.url)
            self.checkQuestion(p.getQuestion())
            self.checkAnswer(p.getAnswers())
        if 'http://answers.yahoo.com' in self.url:
            p = yahoo_answers.parseQAPage(self.url)
            self.checkQuestion(p.getQuestion())
            self.checkAnswer(p.getAnswers())
            
    def checkQuestion(self, question):
        assert question['question_text'] == self.question['question_text'], 'Question text did not match'
        assert question['datetime'] == self.question['datetime'], 'Datetime did not match'
        assert question['user'] == self.question['user'], 'User did not match'
        assert question == self.question, 'Question did not match' # could probably remove this...

    def checkAnswer(self, answer):
        print 'checkAnswer not implemented'



question = {'question_text': 'Are the poor people better off today rather than four years ago?', \
            'user': None, \
            'datetime': 'Posted 3 days ago'}
answer = ''
checkScrape('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250', question, answer)


#checkScrape('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS', \
#                     {'question_text': '', \
#                      'user': '', \
#                      'datetime': ''})


print 'All Tests Passed'









#Sites to use:
# small tests - we should really get a testing package going...
#Anonymous
#pp = parseQAPage('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250')
#Not Anonymous
#pp = parseQAPage('http://aolanswers.com/questions/politics_government_627011121388373')
#lots of answers
#pp = parseQAPage('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250')

#pp.getQuestion()
#pp.getAnswer()

# YAHOO

# small tests - we should really get a testing package going...
#pp = parsePage('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS')

#best answer example
#pp = parseQAPage('http://answers.yahoo.com/question/index?qid=20100224064407AALja9R')

#pp.getQuestion()
#pp.getAnswer()
