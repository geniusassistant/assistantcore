from bs4 import BeautifulSoup
import re
import urllib.request
import random
import json

username = json.load(open('config.json'))["githubusername"]

def latestrepo(uname):
    url = 'https://github.com/'+uname+'?tab=repositories'

    stories = []

    sock = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(sock, "lxml")
    span = soup.findAll("a", { "itemprop" : "name codeRepository" })

    for item in span:
        stripitem = re.findall('>([^"]*)<', str(item))[0]
        if stripitem not in stories:
            stories.append(stripitem)

    return 'https://github.com/'+uname+'/'+stories[0].strip()

def latestmessage(url):

    stories = []

    sock = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(sock, "lxml")
    span = soup.findAll("a", { "class" : "message" })

    for item in span:
        stripitem = re.findall('>([^"]*)<', str(item))[0]
        if stripitem not in stories:
            stories.append(stripitem)

    return stories[0]

def all():
    return latestmessage(latestrepo(username))

def outsource(text):
    if "what's my latest commit" in text:
        return 'in your last commit message, you said ' + all()