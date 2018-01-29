import time
import random

# flips a coin
def flip():
    tof = bool(random.getrandbits(1))
    if tof == True:
        return 'heads'
    else:
        return 'tails'

#main func for api
#TODO: work on transitioning main functions over here
def outsource(text):
    if 'heads or tails' in text:
        return flip()
    if ("what's the time" in text) or ('give me the time' in text):
        timestr = time.strftime("%I o'clock and %M minutes")[1:]
        print(timestr)
        return timestr