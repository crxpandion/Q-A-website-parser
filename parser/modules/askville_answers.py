#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage
import datetime

class parseQAPage(parsePage):
    def getQuestion(self):
        q = {}
	try:
       		question_field = self.dom.find('div', 'question_outer')
        	title = question_field.find('h1', id='question_summary').find(id='question_link').contents[0].lstrip().rstrip()
	except:
		question_field = "N/A"
		title = "N/A"
	try:
        	questionLong = question_field.find('div', id='question_details').contents[0].rstrip().lstrip()
	except:
		questionLong = ""
	try:
       		user = question_field.find('a', 'mininav').contents[0].lstrip().rstrip()
		if user.find(" ") > -1:
			user = "N/A"
	except:
		user = "N/A"
	try:
        	datetime = question_field.find('span', 'byline')['title'].split(' ')
	except:
		datetime = {}
		datetime[0] = "1970-01-01"
		datetime[1] = "00:00"
        q['question_text'] = title + ": " + questionLong
        q['user'] = user
        q['datetime'] = datetime[0] + ' ' + datetime[1] + ':00'
        return q

    def getAnswers(self):
        a = []
        answers = self.dom.findAll('div', 'answer_outer') 
	try:
        	upVotes = self.dom.findAll('div', 'top_vote_bar')
	except:
		upVotes = '0'
        for answer in answers:
            ans = {}
	    try:
                idNum = answer.find('h2', 'answer_summary')
                otherIdNum = answer.find('div', 'answer_post')
	    except:
		idNum = ""
		otherIdNum = ""
            if idNum:
		try:
                	idNum = 'votes_' + str(idNum['id'].replace('answer_summary_', ''))
		except:
			idNum = "N/A"
                ans['upVotes'] = '0'
                for item in upVotes:
                    if str(idNum) == str(item['id']) and item.find('span'):
			try:
                        	ans['upVotes'] = item.find('span').string.rstrip()
			except:
				ans['upVotes'] = '0'
                        break
                    
		try:
                	ans['answer'] = answer.find('h2', 'answer_summary').string.rstrip().lstrip() + unicode(answer.find('div', 'mywrite_content')).replace('<!--  mywrite content -->', '').rstrip().lstrip().replace('\n', '').replace('\t', '').replace('\r', '').replace('<div class="mywrite_content">', '')
		except:
			ans['answer'] = "N/A"
		try:
                	ans['datetime'] = getPostDate(answer.find('div', 'byline').contents[2].rstrip().lstrip())
		except:
			ans['datetime'] = "1970-01-01 00:00:00"
		try:
                	ans['user'] = answer.find('div', 'byline').find('a', 'mininav').string.rstrip().lstrip()        
		except:
			ans['user'] = "N/A"
                a.append(ans)
            elif otherIdNum and answer.find('div', 'byline').find('span', 'byline'):
		try:
                	otherIdNum = 'votes_' + str(int(otherIdNum['id'].replace('bubble_', '')) - 1)
		except:
			otherIdNum = "N/A"
                ans['upVotes'] = '0'
                for item in upVotes:
                    if otherIdNum == str(item['id']) and item.find('span'):
			try:
                        	ans['upVotes'] = item.find('span').string.rstrip()
			except:
				ans['upVotes'] = '0'
                        break
		try:
#                	ans['answer'] = answer.find('div', 'answer_post').contents[0].string.rstrip().lstrip().replace('\n', '').replace('\t', '').replace('\r', '')
			answer1 = str(answer.find('div', 'answer_post').contents[0])
			answer1 += str(answer.find('div', 'answer_post').contents[-1])
			if answer1.find("<br style=") > -1:
				answer1 = answer1[0:answer1.find("<br style=")]	
			answer1 = answer1.rstrip().lstrip().replace('\n', '').replace('\t', '').replace('\r', '')
			answer1 = answer1.replace("<br>", " ")
			ans['answer'] = answer1
		except:
			ans['answer'] = "N/A"
		try:
                	ans['datetime'] = getPostDate(answer.find('div', 'byline').find('span', 'byline').string.rstrip().lstrip())
		except:
			ans['datetime'] = "1970-01-01 00:00:00"
		try:
                	ans['user'] = answer.find('div', 'byline').find('a', 'mininav').string.rstrip().lstrip()
		except:
			ans['user'] = "N/A"
                a.append(ans)
        return a
        
def getPostDate(postedOn):
    if 'year' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[0]) * 365)).split()[0] + ' 00:00:00'        
    elif 'month' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[0]) * 30.5)).split()[0] + ' 00:00:00'
    elif 'day' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[0]))).split()[0] + ' 00:00:00'
    else:
        return str(datetime.datetime.now())
