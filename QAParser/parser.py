import urllib2
from bs4 import BeautifulSoup

def makeDOM(url):
  return BeautifulSoup(urllib2.urlopen(url).read())
  
def getQuestion(DOM):
  return 'not implemented'

def getAnswer(DOM):
  return 'not implemented'

# a simple test
print makeDOM('http://www.december.com/html/demo/hello.html')
