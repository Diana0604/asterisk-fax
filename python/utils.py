import time, os

def countdown(secs):
    while(secs > 0):
        time.sleep(1)
        print(secs)
        secs = secs - 1