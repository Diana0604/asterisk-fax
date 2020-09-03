import time, vlc
import multiprocessing
import pygame


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
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        if self.looping:
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
        
