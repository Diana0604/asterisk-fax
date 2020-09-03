from gpiozero import RGBLED
from colorzero import Color
from time import sleep
from random import randrange
import threading
import debug
import RPi.GPIO as GPIO
leds = RGBLED(17, 27, 22)
leds.color = Color('black')
RED = 0
GREEN = 1
BLUE = 2

debugger = debug.Debug(1)

class Lights(object):
    def __init__(self):
	import RPi.GPIO as GPIO
#        GPIO.setmode(GPIO.BOARD)
#        GPIO.setup(11,GPIO.OUT)
#        GPIO.setup(12,GPIO.OUT)
#        GPIO.setup(13,GPIO.OUT)
 #GPIO.output(05,True)
        #GPIO.output(05,False)
        #print('init')
    
    def calculate_steps(self, init, final):
        def get_int(num):
            return abs(int(10*num))
        return max(get_int(init[RED] - final[RED]), get_int(init[GREEN] - final[GREEN]), get_int(init[BLUE] - final[BLUE]))

    def smooth_change_to(self, final):
        init = leds.value
        #init = (0,0,0)
        if init == final:
            return
        
        steps = self.calculate_steps(init, final)
        step_size_red = (init[RED] - final[RED])/steps
        step_size_green = (init[RED] - final[RED])/steps
        step_size_blue = (init[RED] - final[RED])/steps
        for i in range(steps):
            current_values = leds.value
            new_color = Color(current_values[RED] + step_size_red, current_values[GREEN] + step_size_green, current_values[BLUE] + step_size_blue)
            leds.color = new_color
            sleep(0.5)
        leds.color = Color(final)
    
    def generate_random_values(self, init, final):
        red = init[RED]
        green = init[GREEN]
        blue = init[BLUE]
        if(init[RED] != final[RED]):
            red = randrange(int(10*init[RED]), int(10*final[RED]))*0.1
        if(init[GREEN] != final[GREEN]):
            green = randrange(int(10*init[GREEN]), int(10*final[GREEN]))*0.1
        if(init[BLUE] != final[BLUE]):
            blue = randrange(int(10*init[BLUE]), int(10*final[BLUE]))*0.1
        return (red, green, blue)

    def blinking_change_to(self, final, time = 18):
        init = leds.value
        if init == final:
            return
        def random_sleep(time):
            seconds = randrange(0,time)*0.1
            sleep(seconds)
            return seconds
        time_slept = 0
        while time_slept < time - 1:
            new_values = self.generate_random_values(init, final)
            leds.color = Color(new_values)
            time_slept += random_sleep(4)
            leds.off()
            time_slept += random_sleep(2)
        sleep(time - time_slept)
        leds.color = Color(final)
        debugger.title('final color')

    def iradescent_thread(self):
        self.blinking_change_to((0.3,0,0.3))

    def iradescent(self):
        thread = threading.Thread(target=self.iradescent_thread, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
        return thread

    def red(self):
        self.smooth_change_to((1,0,0))
    def purple(self):
        self.smooth_change_to((0.7,0,0.3))

    def pulse(self):
        leds.pulse()


light = Lights()
nothing = (0,0,0)
red = (1,0,0)
purple = (0.7,0,0.3)
#light.red()
#print(light.calculate_steps(purple, nothing))
