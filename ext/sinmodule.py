from bs4 import BeautifulSoup
import re
import urllib.request
import random

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def getficfromurl(url):
    stories = []

    sock = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(sock, "lxml")
    span = str(soup.findAll("div", { "id" : "chapters" })[0])
    span = cleanhtml(span).strip()
    print(span)

def getfic(tag):
    url = 'https://archiveofourown.org/works/search?utf8=%E2%9C%93&work_search%5Bquery%5D=' + tag

    stories = []

    sock = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(sock, "lxml")
    span = soup.findAll("h4", { "class" : "heading" })

    for item in span:
        try:
            stripitem = item.find('a')['href']
            if item not in stories:
                stories.append('https://archiveofourown.org' + stripitem)
        except:
            t = ''

    return stories

def all(tag):
    getficfromurl(getfic(tag)[0])
