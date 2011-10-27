#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup

def makeDOM(url):
  dom = urllib2.urlopen(url).read()
  return BeautifulSoup(dom)
  
def getQuestion(DOM):
  return 'not implemented'

def getAnswer(DOM):
  return 'not implemented'

#a simple test
print makeDOM('http://www.december.com/html/demo/hello.html')
