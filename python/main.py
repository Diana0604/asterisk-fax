#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import music

DEBUG = 1
currentPath = "/fax/"
#sounds 
OPENING_THEME = currentPath + "audios/speaker/00-arrival.mp3"
BREATHING = currentPath + "audios/speaker/01-breathing.mp3"

threads = []

#play first song
opening = music.Audio(OPENING_THEME)
breathing = music.Audio(BREATHING, 1)

opening.play()

if(DEBUG):
    print('Checkpoint')

threads.append(breathing.play())

for thread in threads:
    thread.join()