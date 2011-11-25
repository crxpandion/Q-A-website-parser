#!/usr/bin/python
import sys, urllib2, re
sys.path.append('modules')

class QA_runner():
  class ParserError(Exception):
    def __init__(self, m):
      self.m = m
    def __str__(self):
      return repr(self.m)

  def __init__(self, path, verbose = False):
    self.path = path
    self.verbose = verbose
    self.parser = self.choose_parser(path)
    self.run()

  def choose_parser(self, path):
    def open_website(path):
      if re.match('(?=http)\w+', path): 
        f = urllib2.urlopen(path)
      else:
        f = open(path, 'r')
      return f.read() 
    self.html = open_website(path)
    if 'on AOL Answers' in self.html:
      import aol_answers as parser
    elif 'Yahoo! Answers' in self.html:
      import yahoo_answers as parser
    elif 'Answer.Ask.com' in self.html:
      import ask_answers as parser
    elif 'Search Askville' in self.html:
      import askville_answers as parser
    else:
      if self.verbose:
        raise parserError('Unrecognized site')
    return parser.parseQAPage(self.html, self.verbose)

  def run(self):
    self.parser.run() 

# When this project is finished this will not be here...handy for debugging though
QA_runner('http://askville.amazon.com/sheryl-crow-version-song-sun/AnswerViewer.do?requestId=8804279', True)
QA_runner('http://askville.amazon.com/formation-sun-dog/AnswerViewer.do?requestId=5657915', True)
QA_runner('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250', False)
QA_runner('http://answers.ask.com/Science/Other/how_big_is_the_sun', False)
QA_runner('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS', False)
QA_runner('http://askville.amazon.com/long-sun-Vitamin-day/AnswerViewer.do?requestId=76403763', False)
QA_runner('http://www.facebook.com')

#Old URLs, should go back and try these
#print parseQAPage(urllib2.urlopen('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250').read()).getQuestion()
#print parseQAPage('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250').getAnswers()
#print parseQAPage('http://answers.ask.com/Science/Other/how_big_is_the_sun').getQuestion()
#print parseQAPage('http://answers.ask.com/Science/Other/how_big_is_the_sun').getAnswers()
#print parseQAPage('http://askville.amazon.com/long-sun-Vitamin-day/AnswerViewer.do?requestId=76403763').getAnswers()
#print parseQAPage('http://askville.amazon.com/sheryl-crow-version-song-sun/AnswerViewer.do?requestId=8804279').getAnswers()
#print parseQAPage('http://askville.amazon.com/formation-sun-dog/AnswerViewer.do?requestId=5657915').getAnswers()
#print parseQAPage('http://askville.amazon.com/Universe-expanding-result-Big-Bang-collapse-start/AnswerViewer.do?requestId=74787617').getAnswers()

