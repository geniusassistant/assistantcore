import time
import random
import news
import gitmessage
import json

def weather():
    import urllib.request
    w = json.loads(urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?id=2653656&units=metric&appid=e5b292ae2f9dae5f29e11499c2d82ece").read())
    const = 'it is ' + str(w['main']['temp']) + ' degrees outside and there is ' + str(w['weather'][0]['description'])
    return const

def bitcoin():
    import urllib.request
    w = json.loads(urllib.request.urlopen("https://bitpay.com/api/rates").read())
    const = "bitcoin's price is " + str(w[3]['rate']).split('.')[0] + ' pounds'
    return const

# flips a coin
def flip():
    tof = bool(random.getrandbits(1))
    if tof == True:
        return 'heads'
    else:
        return 'tails'

#main func for api
def outsource(text):
    if "what's my latest commit" in text:
        return 'in your last commit message, you said ' + gitmessage.all()

    if 'heads or tails' in text:
        return flip()

    if ("what's the time" in text) or ('give me the time' in text):
        timestr = time.strftime("%I o'clock and %M minutes")[1:]
        print(timestr)
        return timestr

    if "what's trending" in text:
        return news.headline()

    if ("who's cool" in text) or ('who is cool' in text):
        return 'dad, of course'

    if 'get me the weather' in text:
        return weather()

    if 'how much is Bitcoin' in text:
        return bitcoin()

#weather()