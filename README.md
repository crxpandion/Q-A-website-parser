Q/A website parser
==================
This is a webscraper designed to scrape question answer websites. This was originally designed to help build tools to determine if a website "shady" based off of the answers in these websites. 
This was a quick hack project for a network security class at Northwestern University. 

Requirements for Using our Tool
===============================
-We recommend running this tool on a Linux operating system with Python version 2.7.2 or later (the BeautifulSoup 4 documentation claims that it will work with Python 3, but this was not tested by us.  Furthermore, we did encounter some issues using Python 2.6; see below).
-BeautifulSoup 4 and MySQLdb are the major third party modules required 
for using our tool.  The BeautifulSoup module is included in the tarball.
-urllib2 is required if pulling HTML directly from URLs is desired.
-The system worked correctly with Ubuntu 11.10, python 2.7.2, and BeautifulSoup 4.



Known Issues/Problems Encountered
=================================
One of our group members was using Mac OS X, and problems persisted throughout the project.  Some of these problems were fixed by upgrading his Python version to 2.7.2, but there are still errors that have not yet been resolved.  These errors appear to be due to major rewrites in BeautifulSoup 4.0 that allow for more flexibility with regard to the user selecting his/her deisred HTML parser.  The BeautilfulSoup 4.0 ReadMe file says the user can choose Python’s standard HTML parser, lxml’s HTML parser, or html5lib’s parser.  We chose to stick with Python’s standard HTML parser; perhaps installing one of the others would resolve these issues.

Architecture
============
The project consists mainly of a QA_runner class which takes a url and parsers it as html. We currently support yahoo answers, ask.com, aol answers, and askville. 
Additional sites can be added to this list by subclassing the parserPage class.
This project need some major clean up to reall be usable.

How to Use our Tool
===================
-Upgrade/Install Python 2.7.2 or later.  Ample instruction on how to do this is available on the Internet
-Install the BeautifulSoup 4 module
uncompress the tarball
cd into the BeautifulSoup-4.0b directory
run “python setup.py install”.  You may need root privileges
-Install the MySQLdb module, if necessary,
to install MySQL
sudo apt-get install mysql-server
to use MySQL with Python
sudo apt-get install mysql-python
update the username and password of mysql in Q-A-website-parser / parser / pageParser.py
-Import the QA_runner file and instantiate an object, for example:
  QA_runner('test_sites/yahoo_answers.html', '', True)
  QA_runner('http://answers.yahoo.com/question/index;_ylt=Av7dHM5LzbXVMewfBcJVBwYjzKIX;_ylv=3?qid=20070519123559AAqxhZf', '', True)
-This will run the appropriate parser and insert everything into the database. If the database doesn’t exist it will throw an error.  If the database exists but the tables dont exist it will attempt to create them and then run.  If they already exist if will add to the existing tables.
Look at the testing.py file inside of modules for an of how to setup testing.



