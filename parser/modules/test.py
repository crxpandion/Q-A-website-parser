#!/usr/bin/python
import yahoo_answers
import aol_answers
import unittest


class checkQuestionScrape(unittest.TestCase):
    def __init__(self, url, question):
        self.url = url
        self.question = question
        self.runTest()
        
    def runTest(self):
        if 'aolanswers.com' in self.url:
            assert aol_answers.parseQAPage(self.url).getQuestion()['question'] == self.question, 'The aol question found did not match'
        if 'answers.yahoo.com' in self.url:
            assert yahoo_answers.parseQAPage(self.url).getQuestion()['question'] == self.question, 'The yahoo question found did not match'
            


#  checkAnswerScrape(unittest.TestCase):
#    def...

checkQuestionScrape('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250', 'Are the poor people better off today rather than four years ago?')
checkQuestionScrape('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS', 'Where were you on 9/11?')
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
