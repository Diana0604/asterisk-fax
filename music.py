import vlc

player = vlc.MediaPlayer("audios/speaker/00-arrival.mp3")
player.play()

while player.is_playing:
     pass