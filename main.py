import speech_recognition as sr
import pygame
import random
import time

# Slightly hacky, what does this even do?
import sys

sys.path.insert(0, 'ext')
sys.path.insert(0, 'mod')

# import hand made modules
import say
import news

#import modloader for custom modifications
import load

# inits speech recognition
r = sr.Recognizer()
#r.energy_threshold=5000

# not in use at moment
def substring_after(s, delim):
    return s.partition(delim)[2]

#plays an mp3 file (not in use)
def play(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

#handles recognised text
def handle(text):
    if text == None:
        return
    #t = substring_after(text, 'Google')

    # List of example queries
    # TODO: Move example queries to an external mod file
    if ("what's the time" in text) or ('give me the time' in text):
        timestr = time.strftime("%I o'clock and %M minutes")[1:]
        print(timestr)
        say.speak(timestr)

    if "what's trending" in text:
        print('NEWS')
        say.speak(news.headline())

    if ("who's cool" in text) or ('who is cool' in text):
        say.speak('dad, of course')

    # Handles modding
    fin = load.outsourcer(text)
    if fin != None:
        say.speak(fin)

# tres to recognise audio
def mainfunction(source):
    global r

    print('listening')

    #return "what's the time" # uncomment ths if working offline

    audio = r.listen(source)

    try:
        user = r.recognize_google(audio)
        return user
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None


# prompts for audio
def prompt():
    with sr.Microphone() as source:
        return mainfunction(source)

# main loop
while 1:
    t = prompt()
    print(t)
    handle(t)