import time, vlc
import multiprocessing

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
    def play_once(self):
        self.player.play()
        time.sleep(1.5)
        duration = self.player.get_length() / 1000
        for i in range(duration):
            time.sleep(1)
    def run(self):
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new(self.sound)
        player.set_media(media)
        player.audio_set_volume(self.volume)
        self.player = player
        self.play_once()
        if(self.looping):
            while True:
                self.play_once()
