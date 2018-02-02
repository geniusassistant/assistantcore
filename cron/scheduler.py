import say
from threading import Timer
import schedule

def speak():
    say.speak('are you till alive?')

schedule.every(1000).seconds.do(speak)

def split():
    schedule.run_pending()
    t = Timer(1.0, speak)  # every 5 seconds
    t.start()

split()