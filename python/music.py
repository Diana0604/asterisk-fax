import time, vlc
import multiprocessing
import pygame


class Controller(object):

    def play(self, sound, background = False, looping = False, volume = 1, music_processes = []):
        if(background):
            process = multiprocessing.Process(target=self.run, args=(sound, background, looping, volume, music_processes)) 
            process.start() 
            return process
        else:
            self.run(sound, background, looping, volume)

    def wait_for_silence(self, music_processes):
        while len(music_processes) > 0:
            print("playing a sound")
            process = music_processes.pop()
            process.join()
        print("not playing")

    def run(self, sound, background, looping, volume, music_processes = []):
        self.wait_for_silence(music_processes)
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        if looping:
            while True:
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
        
