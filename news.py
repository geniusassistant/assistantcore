from bs4 import BeautifulSoup
import re
import urllib.request
import random


def headline():
    url = 'https://www.bbc.co.uk'

    stories = []

    sock = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(sock, "lxml")
    span = soup.findAll("span", { "class" : "top-story__title" })

    for item in span:
        stripitem = re.findall('>([^"]*)<', str(item))[0]
        if stripitem not in stories:
            stories.append(stripitem)

    return random.choice(stories)
