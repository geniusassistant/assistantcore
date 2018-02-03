import say
from threading import Timer
import schedule

def remind(text):
    global sched

    say.speak(text)

    return schedule.CancelJob

def do(self, job_func, *args, **kwargs):
    """Specifies the job_func that should be called every time the
    job runs.
    Any additional arguments are passed on to job_func when
    the job runs.
    :param job_func: The function to be scheduled
    :return: The invoked job instance
    """
    self.job_func = functools.partial(job_func, *args, **kwargs)

def add(time, text):
    schedule.every().day.at(time).do(lambda: remind(text))


def split():
    schedule.run_pending()
    t = Timer(1.0, split)  # every 5 seconds
    t.start()

add(10, 'Remember your glasses tomorrow')
split()