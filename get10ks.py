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


symbol = 'pzza'

edgarurl = "https://sec.report/Document/Search/?formType=10-K&queryCo="+symbol+"#results"

#setup bs4 stuff
headers = {
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'en-US,en;q=0.8',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
}

url=edgarurl 

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url,headers=headers).text


table = pd.read_html(html_content)

print table[0] 



files = pd.read_csv('CompanyList.csv')

print files 




files['downloaded'] = 'N'
for i in range(len(files.Ticker)):
#for i in range(1):
	try:
		ticker = files.Ticker[i]
		print ticker 
		print i 
		link = 'https://sec.report/Document/Search/?formType=10-K&queryCo='+ticker+'#results'


		parser = 'html.parser'
		response = requests.get(link,headers=headers)
		data = response.text.encode("utf-8") 
			
			
		dom =  lxml.html.fromstring(data)

		for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
			#print link
			
			if '2020' in link:
				newlink = link 
			if '2021' in link:
				newlink = link
			if '2022' in link:
				newlink = link
			
		#newlink = dom.xpath('//a/@href')[10]
		#print newlink 

			
		response2 = requests.get(newlink,headers=headers)
		data2 = response2.text.encode("utf-8") 
		
		filename = "10kfull/"+ticker+".txt" 
		with open(filename, 'wb') as f:
			f.write(data2)
			
		files.downloaded.iloc[i] = 'Y'
			
	except:
		continue 
		
	files.to_csv('dllog.csv') 
		
	time.sleep(1)
	




