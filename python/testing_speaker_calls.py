import asterisk, time, vlc

while asterisk.fax_free():
    time.sleep(1)

media_player = vlc.MediaPlayer()
media = vlc.Media("/fax/sounds/fax/03.wav")
media_player.set_media(media)
media_player.play()

time.sleep(2300)