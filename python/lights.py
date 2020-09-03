#as;dfjo
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

    def fade_in_to(self, color, fade_time = 10):
        self.leds.pulse(0, fade_time,self.leds.value, color, 1, True)
        debugger.title('LIGHTS ARE FADING INTO: ' + str(color))

    def pulse(self, fade_in_time=1, fade_out_time=1, n=None, background=True):
        current = self.leds.value
        self.leds.pulse(fade_in_time, fade_out_time, (0, 0, 0), current, n=None, background=True)
        debugger.title('LIGHTS ARE PULSING IN AND OUT OF: ' + str(current))

    def blink_to(self, color, time = 16):
        counter = time*5
        init = self.leds.value
        debugger.title('LIGHTS ARE BLINKING INTO: ' + str(color))
        for i in range(1, counter - 1):
            random_color = (randrange(0,100)*0.01,randrange(0,100)*0.01,randrange(0,100)*0.01)
            random_time = randrange(1,2)*0.1
            self.leds.blink(random_time, 0.2-random_time, 0, 0, init, random_color, 1, False)
        random_time = randrange(1,2)*0.1
        self.leds.blink(random_time, 0.2-random_time, 0, 0, init, color, 1, False)