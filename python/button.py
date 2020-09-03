#from gpiozero import Button
import os, debug, music, calls, threading
from time import sleep
from gpiozero import Button

CURRENT_PATH = ""
if os.uname()[0] != 'Darwin':
    CURRENT_PATH = "/fax/"
FINALE = CURRENT_PATH + "audios/speaker/10-final.mp3"

debugger = debug.Debug(1)

button = Button(26)
def launch_finale():
    debugger.title('LAUNCING FINAL MUSIC')
    music.Audio(FINALE).play()
    debugger.title('LAUNCING FINAL CALL')
    sleep(7)
    calls.dial('08-finale.call')

def wait_for_button():
    debugger.title('BUTTON IS WAITING')
    pressed = False
    while not pressed:
        if button.is_pressed:
            pressed = True
            launch_finale()
            import lights
            lights.Controller()

t1 = threading.Thread(target = wait_for_button)
t1.start()
