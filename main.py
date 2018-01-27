import speech_recognition as sr
import pygame
import say
import time
import news
import random

r = sr.Recognizer()
#r.energy_threshold=5000

def flip():
    tof = bool(random.getrandbits(1))
    if tof == True:
        return 'heads'
    else:
        return 'tails'

def substring_after(s, delim):
    return s.partition(delim)[2]

def play(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def handle(text):
    if text == None:
        return
    #t = substring_after(text, 'Google')

    if ("what's the time" in text) or ('give me the time' in text):
        timestr = time.strftime("%I o'clock and %M minutes")[1:]
        print(timestr)
        say.speak(timestr)

    if "what's trending" in text:
        print('NEWS')
        say.speak(news.headline())

    if ("who's cool" in text) or ('who is cool' in text):
        say.speak('dad, of course')

    if 'heads or tails' in text:
        say.speak(flip())

def mainfunction(source):
    global r

    print('listening')
    audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        user = r.recognize_google(audio)
        return user
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None



def prompt():
    with sr.Microphone() as source:
        while 1:
            return mainfunction(source)

while 1:
    t = prompt()
    print(t)
    handle(t)