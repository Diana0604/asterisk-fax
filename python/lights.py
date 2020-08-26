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
            thread = threading.Thread(target=self.iradescent_thread, args=())
            thread.daemon = True                            # Daemonize thread
            thread.start()                                  # Start the execution
            return thread
    def iradescent_thread(self):
        time_slept = 0
        finalR = 3
        finalG = 0
        finalB = 5
        while time_slept < 17:
                ratio = time_slept*0.01
                ledR.value = finalR*0.1 + randrange(-finalR,finalR)*0.1 #*ratio
#                ledG.value = finalG*0.1 + randrange(-finalG,finalG)*0.1*ratio
                ledB.value = finalB*0.1 + randrange(-finalB,finalB)*0.1 #*ratio
                time1 = 0.1 + randrange(0,4)*0.1
                time_slept += time1
                sleep(time1)
                ledR.value = 0
                ledG.value = 0
                ledB.value = 0
                time2 = 0.1 + randrange(0,4)*0.1
                sleep(time2)
                time_slept += time2
        sleep(18 - time_slept)
        ledR.value = finalR*0.1
        ledG.value = finalG*0.1
        ledB.value = finalB*0.1
    def red(self):
        initR = ledR.value
        initB = ledB.value
        initG = ledG.value
        finalR = 1.0
        finalB = 0.0
        finalG = 0.0
        for i in range (0,7):
            ledR.value = ledR.value + (finalR-initR)/7
            ledB.value = ledB.value + (finalB-initB)/7
            ledG.value = ledG.value + (finalG-initG)/7
            print('ledR: ', ledR.value)
            print('ledG: ', ledG.value)
            print('ledB: ', ledB.value)
            sleep(0.3)


#button.when_pressed = turn_lights_on
#button.when_released = turn_lights_off

