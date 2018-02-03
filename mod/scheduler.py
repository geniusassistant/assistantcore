import say
from threading import Timer
import schedule

def substring_after(s, delim):
    return s.partition(delim)[2]

def remind(text):
    global sched

    say.speak(text)

    return schedule.CancelJob

def do(self, job_func, *args, **kwargs):
    self.job_func = functools.partial(job_func, *args, **kwargs)

def add(time, text):
    schedule.every().day.at(time).do(lambda: remind(text))


def split():
    schedule.run_pending()
    t = Timer(1.0, split)  # every 5 seconds
    t.start()


def outsource(text):
    if 'add to my schedule' in text:
        message = text.replace('add to my schedule', '').replace(substring_after(text, 'at'), '').replace('at', '')

        add(substring_after(text, 'at'), message)
        return 'added ' + message + 'to your schedule'

split()