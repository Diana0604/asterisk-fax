from gpiozero import RGBLED
from colorzero import Color
from time import sleep
from random import randrange
import debug
import RPi.GPIO as GPIO

RED = 0
GREEN = 1
BLUE = 2

debugger = debug.Debug(1)

class Lights(object):

    def __init__(self):
        self.leds = RGBLED(24, 27, 22)

    def change_color(self, color):
        self.leds.color = Color(color)

    
