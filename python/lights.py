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

class Controller(object):

    def __init__(self):
        self.leds = RGBLED(24, 27, 22)

    def change_color(self, color):
        self.leds.color = Color(color)

    def fade_in_to(self, color, fade_time = 60):
        self.leds.pulse(0, fade_time,self.leds.value, color, 1, True)

    def blink_to(self, color, blink_time = 10):
        self.leds.blink(0.25, 0.25, 0, 0, self.leds.value, color, blink_time, False)
        self.leds.blink(0.25, 0.25, 0, 0, self.leds.value, color, blink_time, False)
        self.leds.blink(0.25, 0.25, 0, 0, self.leds.value, color, blink_time, False)
        self.leds.blink(0.25, 0.25, 0, 0, self.leds.value, color, blink_time, False)
        self.leds.blink(0.25, 0.25, 0, 0, self.leds.value, color, blink_time, False)

