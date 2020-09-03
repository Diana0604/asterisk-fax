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
        self.leds.color = Color('black')

    def calculate_steps(self, init, final):
        def get_int(num):
            return abs(int(100*num))
        return max(get_int(init[RED] - final[RED]), get_int(init[GREEN] - final[GREEN]), get_int(init[BLUE] - final[BLUE]))

    def smooth_change_to(self, final):
        init = self.leds.value
        if init == final:
            return
        steps = self.calculate_steps(init, final)
        step_size_red = (final[RED] - init[RED])/steps
        step_size_green = (final[GREEN] - init[GREEN])/steps
        step_size_blue = (final[BLUE] - init[BLUE])/steps
        for i in range(steps):
            current_values = self.leds.value
            next_red = current_values[RED] + step_size_red
            next_green = current_values[GREEN] + step_size_green
            next_blue = current_values[BLUE] + step_size_blue
            new_color = Color(next_red, next_green, next_blue)
            self.leds.color = new_color
            sleep(0.1)
        self.leds.color = Color(final)
    
    def generate_random_values(self, init, final):
        def get_random(num1, num2):
            min_num = min(num1, num2)
            max_num = max(num1, num2)
            return randrange(min_num,max_num)
        red = init[RED]
        green = init[GREEN]
        blue = init[BLUE]
        if(init[RED] - final[RED] > 0.1):
            red = get_random(int(10*init[RED]), int(10*final[RED]))*0.1
        if(init[GREEN] - final[GREEN] > 0.1):
            green = get_random(int(10*init[GREEN]), int(10*final[GREEN]))*0.1
        if(init[BLUE] - final[BLUE] > 0.1):
            blue = get_random(int(10*init[BLUE]), int(10*final[BLUE]))*0.1
        return (red, green, blue)

    def blinking_change_to(self, final, time = 18):
        init = self.leds.value
        if init == final:
            return
        def random_sleep(time):
            seconds = randrange(0,time)*0.1
            sleep(seconds)
            return seconds
        time_slept = 0
        while time_slept < time - 1:
            new_values = self.generate_random_values(init, final)
            self.leds.color = Color(new_values)
            time_slept += random_sleep(4)
            self.leds.off()
            time_slept += random_sleep(2)
        sleep(time - time_slept)
        self.leds.color = Color(final)
        debugger.title('final color')

    def iradescent_thread(self):
        self.blinking_change_to((0.3,0,0.3))

    def iradescent_blink(self):
        self.iradescent_thread()

    def red(self):
        self.smooth_change_to((1,0,0))
    def purple(self):
        self.smooth_change_to((0.7,0,0.3))

    def pulse(self):
        self.leds.pulse()
