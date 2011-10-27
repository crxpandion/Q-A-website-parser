#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup

class parsePage:
  def __init__(self, url):
    self.url = url
    self.dom = self.makeDOM()

  def makeDOM(self):
    return BeautifulSoup(urllib2.urlopen(self.url).read())
  
  def getQuestion(self):
    print 'not implemented'

  def getAnswer(self):
    print 'not implemented'

# a simple test
p = parsePage('http://www.december.com/html/demo/hello.html')
print p.dom

