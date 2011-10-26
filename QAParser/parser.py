import urllib2
from xml.dom.minidom import parse

def makeDOM(url):
  dom = urllib2.urlopen(url).read()
  return parse(dom)
  
def getQuestion(DOM):
  return 'not implemented'

def getAnswer(DOM):
  return 'not implemented'

print makeDOM('http://www.google.com')
