import speech_recognition as sr
import pygame
import random
import time

# TODO: add logging for history of speaking

# Slightly hacky, what does this even do?
import sys

sys.path.insert(0, 'ext')
sys.path.insert(0, 'mod')

# import hand made modules
import say

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

def log(input, response):
    with open('log.txt', 'a+') as f:
        f.write(input + ' : ' + response + '\n')

#handles recognised text
def handle(text):
    if text == None:
        return
    #text = substring_after(text, 'Google')

    # Handles modding
    fin = load.outsourcer(text)
    if fin != None:
        log(text, fin)
        say.speak(fin)

# tres to recognise audio
def mainfunction(source):
    global r

    print('getting audio')

    # return "add to my schedule remember your glasses tommorrow at 16:24" # uncomment ths if working offline

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
    print('---')