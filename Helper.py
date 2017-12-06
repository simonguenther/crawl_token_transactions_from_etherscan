import urllib
import sys
import json
import codecs
import re
import cfscrape
from bs4 import BeautifulSoup

#get HTML from link
def get_html(url):
    try:
        return urllib.urlopen(url).read()
    except StandardError as e:
        print "Error getting HTML: " + str(e)

def get_html_cloud(url):
    try:
        scraper = cfscrape.create_scraper()
        return scraper.get(url).content
    except StandardError as e:
        print "Error getting HTML: " + str(e)

def save_list_to_file(path, thelist):
    thefile = open(path, 'w')
    for item in thelist:
        thefile.write("%s\n" % item)

def load_dictionary_from_json(file):
    with open (file) as data_file:
        return json.load(data_file)

def save_dictionary_to_json(path, jsonDump):
	with codecs.open(path,'w','utf-8') as f:
		f.write(json.dumps(jsonDump, indent=3))

def strip_domain(domain, single):
    output = re.sub(domain,"",single)
    return output.strip("/")

def add_to_file(path, item):
    with open(path, "a") as myfile:
         myfile.write("%s\n" % item)
         