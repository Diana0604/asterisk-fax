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

def turn_lights_on():
        for i in range (0,10):
                ledR.value = 0.5 + randrange(-2,3)*0.1
                ledG.value = 0.5 + randrange(-2,3)*0.1
                ledB.value = 0.5 + randrange(-2,3)*0.1
                sleep(0.1 + randrange(0,4)*0.1)
                ledR.value = 0
                ledG.value = 0
                ledB.value = 0
		sleep(0.3)
		sleep(0.1 + randrange(0,2)*0.1)

def turn_lights_off():
        ledR.value = 0
        ledG.value = 0
        ledB.value = 0

#button.when_pressed = turn_lights_on
#button.when_released = turn_lights_off

turn_lights_on()

pause()

