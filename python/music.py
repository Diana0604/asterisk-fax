import time, vlc, threading

def stop_all_music():
    vlc.MediaPlayer().stop()

class Audio(object):
    def __init__(self, sound, background = 0, volume = 100):
        self.background = background
        self.sound = sound
        self.volume = 100

    def play(self):
        if(self.background == 1):
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True                            # Daemonize thread
            thread.start()                                  # Start the execution
            return thread
        else:
            self.run()
    def run(self):
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new(self.sound)
        player.set_media(media)
        player.audio_set_volume(self.volume) 
        player.play()
        time.sleep(1.5)
        duration = player.get_length() / 1000
        time.sleep(duration)

