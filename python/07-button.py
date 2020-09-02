#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

debugger = debug.Debug(1)
currentPath = "/fax/"
#sounds
SOUND12 = currentPath + "audios/speaker/05-sound12.mp3"
SOUND13 = currentPath + "audios/speaker/06-sound13.mp3"
SOUND14 = currentPath + "audios/speaker/07-sound14.mp3"
SOUND15 = currentPath + "audios/speaker/08-sound15.mp3"
TBL_MONOLOGUE = currentPath + "audios/speaker/09-tbl.mp3"
FINALE = currentPath + "audios/speaker/10-final.mp3"
threads = []
#lights
from gpiozero import Button
button = Button(26)
def launch_finale():
    print('finale')
    music.Audio(FINALE).play()

pressed = False
while not pressed:
    if button.is_pressed:
        pressed = True
        launch_finale()
