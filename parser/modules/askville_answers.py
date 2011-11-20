#!/usr/bin/python
import sys
sys.path.append('..')
from bs4 import BeautifulSoup
from pageParser import parsePage
import datetime

class parseQAPage(parsePage):
	def getQuestion(self):
		q = {}
		question_field = self.dom.find('div', 'question_outer')
		title = question_field.find('h1', id='question_summary').find(id='question_link').contents[0].lstrip().rstrip()
		questionLong = question_field.find('div', id='question_details').contents[0].rstrip().lstrip()
		user = question_field.find('a', 'mininav').contents[0].lstrip().rstrip()
		datetime = question_field.find('span', 'byline')['title'].split(' ')
		q['question_text'] = title + ": " + questionLong
		q['user'] = user
		q['datetime'] = datetime[0] + ' ' + datetime[1] + ':00'
		return q

	def getAnswers(self):
	    a = []
	    answers = self.dom.findAll('div', 'answer_outer')
	    upVotes = self.dom.findAll('div', 'top_vote_bar')
	    for answer in answers:
	        ans = {}
	        idNum = 'votes_' + str(answer.find('h2', 'answer_summary')['id'].replace('answer_summary_', ''))
	        for item in upVotes:
	            if str(idNum) == str(item['id']):
	                ans['upVotes'] = item.find('span').string.rstrip()
	                break
	        if not ans['upVotes']:
	            ans['upVotes'] = '0'
	        ans['answer'] = answer.find('h2', 'answer_summary').string + unicode(answer.find('div', 'mywrite_content')).replace('<!--  mywrite content -->', '')
	        ans['datetime'] = getPostDate(answer.find('div', 'byline').contents[2].rstrip().lstrip())
	        ans['user'] = answer.find('div', 'byline').find('a', 'mininav').string.rstrip().lstrip()        
	        a.append(ans)
	    return a
	    
def getPostDate(postedOn):
    if 'years' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[0]) * 365)).split()[0] + ' 00:00:00'        
    elif 'months' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[0]) * 30.5)).split()[0] + ' 00:00:00'
    elif 'days' in postedOn:
        return str(datetime.datetime.now() - datetime.timedelta(days=int(postedOn.split()[1]))).split()[0] + ' 00:00:00'
    else:
        return str(datetime.datetime.now())

	    
#	    Jesse's Code - I just wanted to shorten it up a bit
#		a = []
#		upvList = []
#		answers = self.dom.findAll('div', 'answer_outer')
#		usersUpvotes = self.dom.findAll('div', 'answer_nickbar')
#		for userUpvote in usersUpvotes:
#			# upvList is used to keep track of the upvotes for each user, and is
#			# in a different for loop since this info appears outside of the
#			# answer_outer block
#			userUpVotesCoord = {}
#			newuser = str(userUpvote.contents[0]).replace('Answer from ','').lstrip().rstrip()
#			userUpVotesCoord['user'] = newuser
#			upVote = userUpvote.next.next.next
#			upVoteSpan = len(upVote('span'))
#			if upVoteSpan > 0:
#				upVoteSpan = upVote.contents[1].contents[0]
#			userUpVotesCoord['upVotes'] = upVoteSpan
#			upvList.append(userUpVotesCoord)
#		for answer in answers:
#			# the answers in askville are styled as a conversation.. after the initial
#			# answer, the person who asked the question and the answerer can comment
#			# on the original answer.  We just want to extract the original answer
#			# and not the conversation.  In order to do that we need to add the users
#			# who answered to a list and make sure that if that any specific user
#			# can't have multiple answers
#			ans = {}

#			# find the user and date first
#			user = answer.find('div', 'byline')
#			datetime = user.find('span', 'byline')['title'].split(' ')
#			user = user.find('a', 'mininav').contents[0].lstrip().rstrip()

#			userSeen = False
#			for x in a:
#				if user in x['user']:
#					userSeen = True
#					break
#			# if we haven't seen this user yet collect the answer
#			if userSeen == False:
#				ans['user'] = user
#				ans['datetime'] = datetime[0] + ' ' + datetime[1]
#			
#				content0 = answer.find('div', 'answer_post qa_bubble').contents[0].lstrip().rstrip()
#				content1 = answer.find('div', 'answer_post qa_bubble').contents[1]
#				content0 = str(content0)
#				content1 = str(content1).replace('<br>',' ')
#				if '<br style=' in content1:
#					# strip away the junk from content1
#					content1 = content1[0:content1.find('<br style=')] 

#				ans['answer'] = (content0 + content1).lstrip().rstrip()

#				ans['upVotes'] = 0  # initialize to 0
#				# now search for the matching upVotes
#				for userUV in upvList:
#					if userUV['user'] == user:
#						ans['upVotes'] = userUV['upVotes']
#				a.append(ans)
#        for x in a:
#            print x['user']
#            print x['datetime']
#            print x['upVotes']
#            print x['answer']
#            print '------------------------------------------------------'
#		return a
		
parseQAPage('http://askville.amazon.com/formation-sun-dog/AnswerViewer.do?requestId=5657915').getAnswers()
