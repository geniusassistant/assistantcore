import requests
from bs4 import BeautifulSoup
import re

def google(text):
    r = requests.get('http://google.com/search?q='+text.replace(' ', '+')).text

    soup = BeautifulSoup(r, "lxml")
    span = soup.findAll("span", { "class" : "_m3b" })
    stripitem = re.findall('>([^"]*)<', str(span))[0]

    return stripitem

def outsource(text):
    if text.startswith('who'):
        return google(text)