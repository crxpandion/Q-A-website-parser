#!/usr/bin/python
import sys, urllib2, re
sys.path.append('modules')
import yahoo_answers as yahoo
import aol_answers as aol
import askville_answers as amazon
import ask_answers as ask

class QA():
    def __init__(self, html, verbose = True):
        self.html = html
        self.verbose = verbose
        self.run()
        
    def run(self):
        if 'on AOL Answers' in self.html:
            aol.parseQAPage(self.html, self.verbose).run()
        elif 'Yahoo! Answers' in self.html:
            yahoo.parseQAPage(self.html, self.verbose).run()
        elif 'Answers.Ask.com' in self.html:
     	    ask.parseQAPage(self.html, self.verbose).run()
     	elif 'Search Askville' in self.html:
     	    amazon.parseQAPage(self.html, self.verbose).run()
     	else:
     	    print 'Site is not recognized'

QA(urllib2.urlopen('http://aolanswers.com/questions/poor_people_better_today_four_years_735670198934250').read(), False)
QA(urllib2.urlopen('http://answers.ask.com/Science/Other/how_big_is_the_sun').read(), False)
QA(urllib2.urlopen('http://answers.yahoo.com/question/index;_ylt=Ai47Sv1EzW5EmuoBQIq9m.Oe5HNG;_ylv=3?qid=20110907120254AALqqeS').read(), True)
QA(urllib2.urlopen('http://askville.amazon.com/long-sun-Vitamin-day/AnswerViewer.do?requestId=76403763').read(), True)
QA(urllib2.urlopen('http://www.facebook.com').read())
