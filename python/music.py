import time, vlc
import multiprocessing
#from pygame import mixer
from playsound import playsound

class Audio(object):
    def __init__(self, sound, background = False, looping = False, volume = 100):
        self.background = background
        self.sound = sound
        self.volume = 100
        self.looping = looping

    def play(self):
        if(self.background):
            process = multiprocessing.Process(target=self.run, args=()) 
            process.start() 
            return process
        else:
            self.run()

    def run(self):
        playsound(self.sound)
        if self.looping:
            while True:
                playsound(self.sound)
