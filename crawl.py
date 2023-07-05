from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.parse import urljoin
from collections import Counter
import string
import re
import requests

#makes sure not to print out any html tags
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
	
#takes all visible text from page, counts term frequency and prints to file	
def text_from_html(body):
	soup = BeautifulSoup(body, 'html.parser')
	texts = soup.findAll(text=True)
	visible_texts = filter(tag_visible, texts)  
	
	paragraph = u" ".join(t.strip() for t in visible_texts)
	
	paragraph = re.sub("[^\w]", " ", paragraph).split()
	counts = Counter(paragraph)
	counts = str(counts)
	text_file.write(counts + "\n")
	
#get the links and prints to file and call function to get text
def url_list(body):
	soup2 = BeautifulSoup(body, 'lxml')
	for link in soup2.find_all('a'):
		x = urljoin(url2,link.get('href'))
		text_file.write("   " + x)
		r2 = requests.get(x)
		data2 = r2.text
		text_from_html(data2)	

	
#asks for user input, opens a file and calls function to get links	
url = input("Enter a website to extract the URL's from: ")
url2= ("http://" + url)
r  = requests.get(url2)
data = r.text

text_file = open("chacon_marisol.txt", "w", encoding = "utf-8")
text_file.write(url2)
text_from_html(data)
url_list(data)
text_file.close()
