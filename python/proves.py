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

ledR.value = 0.5
ledG.value = 0.5
    ledB.value = 0.5

#button.when_pressed = turn_lights_on
#button.when_released = turn_lights_off

