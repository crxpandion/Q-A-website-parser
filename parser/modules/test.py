#!/usr/bin/python
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
            self.checkQuestionAndAnswer(aol_answers.parseQAPage(self.url))
        if 'http://answers.yahoo.com' in self.url:
            self.checkQuestionAndAnswer(yahoo_answers.parseQAPage(self.url))
        if 'http://www.ask.com/answers/' in self.url:
	    self.checkQuestionAndAnswer(ask_answers.parseQAPage(self.url))
        if 'http://answers.ask.com/' in self.url:
     	    self.checkQuestionAndAnswer(ask_answers.parseQAPage(self.url))
     	if 'http://askville.amazon.com/' in self.url:
     	    self.checkQuestionAndAnswer(askville_answers.parseQAPage(self.url))

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


# Askville from Amazon
#question = {'question_text': 'Will the Universe keep expanding?', \
# 'user': 'NormanL', \
# 'datetime': '12 months ago'}
#answer = ''
#checkScrape('http://askville.amazon.com/formation-sun-dog/AnswerViewer.do?requestId=5657915', question, answer)

# Ask
#question = {'question_text': 'What is the longest River?', \
# 'user': 'eilleenc', \
# 'datetime': 'Posted 2 months ago'}
#answer = ''
#checkScrape('http://answers.ask.com/Science/Other/how_big_is_the_sun', question, answer)


# AOL - no user
question = {'question_text': 'Are the poor people better off today rather than four years ago?', \
            'user': None, \
            'datetime': '2011-10-26 00:00:00'}
answer = {'answer': 'I think in general, you have a few marbles loose upstairs.....You must of been dong some heavy relaps in drugs, or slept for all those years.....Good, Mr. Van Winkle...', \
          'upVotes': '0', \
          'datetime': '2011-10-26 00:00:00'}
checkScrape('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250', question, answer)


# Yahoo
#question = {'question_text': 'Where were you on 9/11? Sunday marks the tenth anniversary of the 9/11 attacks. We know that it\'s still in everyone\'s memory. Please share with us your recollections. What do you remember most about that day?', \
# 'user': 'profile-AA10030221', \
# 'datetime': '2011-09-07 19:02:54'}
#answer = ''
#checkScrape('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS', question, answer)

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
