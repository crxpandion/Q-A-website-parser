#!/usr/bin/python
import sys, urllib2, re
sys.path.append('modules')

class ParserError(Exception):
    def __init__(self, value):
      self.value = value
    def __str__(self):
      return repr(self.value)

class QA_runner():
  def __init__(self, path, html, verbose = False):
    self.path = path
    self.verbose = verbose
    self.html = html
    try:
      self.parser = self.choose_parser(path, html)
      self.run()
    except ParserError, m:
      if self.verbose:
        print m.value
    except:
      raise

  def choose_parser(self, path, html):
    def open_website(path):
      if re.match('(?=http)\w+', path): 
        f = urllib2.urlopen(path)
      else:
        f = open(path, 'r')
      return f.read()
    if path:
      self.html = open_website(path)
    if 'on AOL Answers' in self.html:
      import aol_answers as p
    elif 'Yahoo! Answers' in self.html:
      import yahoo_answers as p
    elif 'Answers.Ask.com' in self.html:
      import ask_answers as p
    elif 'Search Askville' in self.html:
      import askville_answers as p
    else:
      raise ParserError('\nError: could not recognize site')
    return p.parseQAPage(self.html, self.path, self.verbose)

  def run(self):
    self.parser.run() 

# Demos
# Working
QA_runner('test_sites/aol_answers.html', '', True)

QA_runner('http://answers.yahoo.com/question/index;_ylt=Av7dHM5LzbXVMewfBcJVBwYjzKIX;_ylv=3?qid=20070519123559AAqxhZf', '', True)

# NOT WORKING
#QA_runner('test_sites/yahoo_answers.html', '', True)

# WORKING
QA_runner('http://askville.amazon.com/long-sun-Vitamin-day/AnswerViewer.do?requestId=76403763', '', True)

# NOT WORKING
#QA_runner('http://askville.amazon.com/sheryl-crow-version-song-sun/AnswerViewer.do?requestId=8804279', '', True)

# NOT WORKING
#QA_runner('http://answers.ask.com/Science/Other/how_big_is_the_sun', '', True)

# ERROR URL
QA_runner('http://www.facebook.com', '', True)

print "\nFinished"


#drop database qaparser
#create database qaparser
