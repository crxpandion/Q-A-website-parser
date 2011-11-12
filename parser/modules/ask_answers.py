#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage

class parseQAPage(parsePage):
	def getQuestion(self):
		q = {}
		print self.dom.__str__()
		#print self.dom.prettify()
		question_field = self.dom.find('div', id='qnaQuesComm')
		title = question_field.find('div', 'txt_xxlg abstract pl15 pb10').contents[0].lstrip().rstrip()
		user = question_field.find('div', 'rr_life_title b').contents[0].replace(' asked','')
		q['question_text'] = title
		q['user'] = user
		q['datetime'] = 'not_given'
		#print title;
		#print question_field.prettify()
		#question_field = self.dom.find(attrs={"div": "class='question'"})
		#print question_field
		#title = question_field.find('p', 'questionText').contents[0].lstrip().rstrip()
		#user = question_field.find('div', class='rr_life_title b').contents[0].lstrip().rstrip()
		#print user
		#q['question text'] = title
		#q['user'] = user
		#print "Question:"
		#print q['question_text']
		#print "User:"
		#print q['user']
		return q
