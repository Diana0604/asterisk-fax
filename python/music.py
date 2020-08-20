#REMEMBER TO CHANGE TO /fax BEFORE GITTING

import time, vlc

def Play(sound):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(sound)
    player.set_media(media)
    player.play()
    time.sleep(1.5)
    duration = player.get_length() / 1000
    time.sleep(duration)