import time, vlc
import multiprocessing
import pygame
import debug

debugger = debug.Debug(1)

class Controller(object):
    def __init__(self):
        self.music_processes = []

    def new_music_process(self, process):
        self.kill_all_processes()
        self.music_processes.append(process)

    def kill_all_processes(self):
        debugger.title('KILLING PROCESSES')
        while len(self.music_processes) != 0:
            self.music_processes.pop().terminate()


    def play(self, sound, background = False, looping = False, volume = 1):
        if(background):
            process = multiprocessing.Process(target=self.run, args=(sound, background, looping, volume)) 
            process.start()
            self.new_music_process(process)
            return process
        else:
            self.kill_all_processes()
            self.run(sound, background, looping, volume)

    def wait_for_silence(self):
        while len(self.music_processes) > 0:
            process = self.music_processes.pop()
            process.join()

    def run(self, sound, background, looping, volume):
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
        
