#LED STRIP WHERE R - 17 G - 27 B - 22
#BUTTONS CONNECTED TO PIN 23
from gpiozero import PWMLED
from gpiozero import Button
from signal import pause
from time import sleep
from random import randrange

ledR = PWMLED(17)
ledG = PWMLED(27)
ledB = PWMLED(22)

button = Button(23)
import time, vlc, threading

class Lights(object):
    def __init__(self, background = 1):
        self.background = background

    def iradescent(self):
        if(self.background == 1):
            thread = threading.Thread(target=self.iradescent_thread, args=())
            thread.daemon = True                            # Daemonize thread
            thread.start()                                  # Start the execution
            return thread
        else:
            self.run()
    def iradescent_thread(self):
        time_slept = 0
        while time_slept < 25:
                ledR.value = 0.5 + randrange(-2,3)*0.1
                ledG.value = 0.5 + randrange(-2,3)*0.1
                ledB.value = 0.5 + randrange(-2,3)*0.1
                time1 = 0.1 + randrange(0,4)*0.1
                time_slept += time1
                sleep(time1)
                ledR.value = 0
                ledG.value = 0
                ledB.value = 0
                time2 = 0.1 + randrange(0,4)*0.1
                sleep(time2)
                time_slept += time2
        sleep(26 - time_slept)
        ledR.value = 0.5
        ledG.value = 0.5
        ledB.value = 0.5

#button.when_pressed = turn_lights_on
#button.when_released = turn_lights_off

