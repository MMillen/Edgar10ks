import csv
import requests
import xml.etree.ElementTree as ET
import re 
import pandas as pd 
from bs4 import BeautifulSoup, SoupStrainer
from lxml import etree 
import urllib2 
import warnings; warnings.filterwarnings(action='once')
from lxml import html 
import requests 
import time
from bs4.dammit import EncodingDetector
import lxml.html
from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
 
class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text


files = pd.read_csv('CompanyList.csv')
log = pd.DataFrame(columns=['ticker','found','text']) 

#for i in range(len(files.Ticker)):
for i in range(10):

	symbol = files.Ticker[i]
	try:
		with open("10kfull/"+symbol+".txt", "r") as f:
			text= f.read()
			lines = f.readlines() 
			
			


		
		s = text
		s2 = "Human Capital</"
		s3 = "Human Capital </"
		s4 = "Human Capital Resources</"
		s5 = "Human Capital Resources </"
		
		
		#add these 
		s6 = "Human Capital Management</"
		s7 = "Human Capital Management </"
		
		
		if s.find(s2) > 1000:
			
			text2 = text[s.find(s2):s.find(s2)+30000]
			
			txt = dehtml(text2)
			
			log = log.append({'ticker':symbol,'found':'Y', 'text':txt}, ignore_index=True)
			
			
			
			
		if s.find(s3) > 1000:
			
			text2 = text[s.find(s3):s.find(s3)+30000]
			
			#print dehtml(text2) 
			txt = dehtml(text2)
			
			log = log.append({'ticker':symbol,'found':'Y', 'text':txt}, ignore_index=True)
			
			
		if s.find(s4) > 1000:
			
			text2 = text[s.find(s3):s.find(s3)+30000]
			
			#print dehtml(text2) 
			txt = dehtml(text2)
			
			log = log.append({'ticker':symbol,'found':'Y', 'text':txt}, ignore_index=True)
			
			
		if s.find(s5) > 1000:
			
			text2 = text[s.find(s3):s.find(s3)+30000]
			
			#print dehtml(text2) 
			txt = dehtml(text2)
			
			log = log.append({'ticker':symbol,'found':'Y', 'text':txt}, ignore_index=True)
			
			
		log.to_csv('parselog.csv') 
		
		print log 
		
	except:
		continue 



	