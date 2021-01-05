#from gpiozero import PWMLED
from gpiozero import RGBLED
#led = RGBLED(2, 3, 4)
from time import sleep
import os, utils
Red = 17
Green = 27
Blue = 22

led = RGBLED(Red, Green, Blue)

class TransitioningLights:
    def __init__(self, instructions):
        i = 1
        self.number = 1
        if instructions[i] == "number":
            self.number = int(instructions[i+1])
            i = i + 2
        if instructions[i] == "time":
            self.time = float(instructions[i+1])/float(self.number)
            i = i + 2
        self.iterations = []
        for n in range(0, self.number):
            new_transition = {}
            if instructions[i] == "from":
                Red = float(instructions[i+1])
                Green = float(instructions[i+2])
                Blue = float(instructions[i+3])
                new_transition["init"] = (Red, Green, Blue)
                i = i + 4
            if instructions[i] == "to":
                Red = float(instructions[i+1])
                Green = float(instructions[i+2])
                Blue = float(instructions[i+3])
                new_transition["final"] = (Red, Green, Blue)
                i = i + 3
            self.iterations.append(new_transition)
            i = i + 1
        if instructions[i] == "time":
            self.time = float(instructions[i+1])/self.number
    def start(self):
        transition = self.iterations[0]
        led.pulse(fade_in_time=0, fade_out_time=self.time, on_color=transition["init"], off_color=transition["final"], n=1, background=True)
        self.number = self.number - 1
        self.iterations.pop(0)
        return self.time

class BlinkingLights:
    def __init__(self, instructions):
        i = 1
        while i < len(instructions):
            if instructions[i] == "color":
                Red = float(instructions[i+1])
                Green = float(instructions[i+2])
                Blue = float(instructions[i+3])
                self.color = (Red, Green, Blue)
                i = i + 3
            if instructions[i] == "times":
                self.times = int(instructions[i+1])
                self.time = 4*self.times
                i = i + 1
            i = i + 1
    def start(self):
        led.blink(on_time=3, off_time=1, fade_in_time=0, fade_out_time=0, on_color=self.color, off_color=led.color, n=self.times, background=True)
        return self.time

class TwinkleLights:
    def __init__(self, instructions):
        i = 1
        while i < len(instructions):
            if instructions[i] == "on_color":
                on_Red = float(instructions[i+1])
                on_Green = float(instructions[i+2])
                on_Blue = float(instructions[i+3])
                self.on_color = (on_Red, on_Green, on_Blue)
                i = i + 3
            if instructions[i] == "off_color":
                off_Red = float(instructions[i+1])
                off_Green = float(instructions[i+2])
                off_Blue = float(instructions[i+3])
                self.off_color = (off_Red, off_Green, off_Blue)
                i = i + 3
            if instructions[i] == "time":
                self.time = float(instructions[i+1])
                i = i + 1
            i = i + 1
    def start(self):
        led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0, on_color=self.on_color, off_color=self.off_color, n=int(self.time/2), background=True)
        return self.time

class PulsingLights:
    def __init__(self, instructions):
        i = 1
        while i < len(instructions):
            if instructions[i] == "color":
                Red = float(instructions[i+1])
                Green = float(instructions[i+1])
                Blue = float(instructions[i+3])
                self.color = (Red, Green, Blue)
                i = i + 3
            i = i + 1
    def start(self):
        led.color = (0.1,0.1,0.1)
        led.pulse(fade_in_time=2, fade_out_time=2, on_color=self.color, off_color=(0.1, 0.1, 0.1), n=None, background=True)

class ConstantLights:
    def __init__(self, instructions):
        i = 1
        while i < len(instructions):
            if instructions[i] == "color":
                Red = float(instructions[i+1])
                Green = float(instructions[i+2])
                Blue = float(instructions[i+3])
                self.color = (Red, Green, Blue)
                i = i + 3
            i = i + 1
    def start(self):
        led.color = self.color

def instructions_to_lights(instructions):
    if instructions[0] == "transition":
        return TransitioningLights(instructions)
    if instructions[0] == "blink":
        return BlinkingLights(instructions)
    if instructions[0] == "twinkle":
        return TwinkleLights(instructions)
    if instructions[0] == "pulse":
        return PulsingLights(instructions)
    if instructions [0] == "constant":
        return ConstantLights(instructions)

LIGHTS_PATH = '/fax/lights/'
DIEGETIC_LIGHTS_PATH = LIGHTS_PATH + 'diegetic/'
BACKGROUND_LIGHTS_PATH = LIGHTS_PATH + 'background/'
background_lights = os.listdir(BACKGROUND_LIGHTS_PATH)
diegetic_lights = os.listdir(DIEGETIC_LIGHTS_PATH)

DIEGETIC_LIGHTS_ON = False

led.color = (0,0,0)

previous_step = None
diegetic_processes = []
unfinished_transitions = []

def get_diegetic_lights(step):
    if previous_step == step:
        return None
    for lights in diegetic_lights:
        if lights.startswith(step):
            print('found: ' + lights)
            return lights
    return None

def get_background_lights(step):
    if previous_step == step: 
        return None
    for lights in background_lights:
        initial_step = lights[0] + lights[1]
        last_step = lights[3] + lights[4]
        if initial_step <= step and last_step >= step:
            return lights
    return None

def read_file(file):
    f = open(file)
    return f.read().split()

from multiprocessing import Process

def launch_diegetic_lights(step):
    global previous_step
    global diegetic_processes
    print(previous_step)
    print(step)
    if(previous_step == step):
        return False
    lights_file = get_diegetic_lights(step)
    if lights_file == None:
        return False
    instructions = read_file(DIEGETIC_LIGHTS_PATH + lights_file)
    if len(instructions) == 0:
        return False
    diegetic_light = instructions_to_lights(instructions)
    time = diegetic_light.start()
    process = Process(target=utils.countdown, args=(time,))
    process.start()
    if diegetic_light.number != None and diegetic_light.number > 0:
        unfinished_transitions.append(diegetic_light)
    diegetic_processes.append(process)
    global DIEGETIC_LIGHTS_ON
    DIEGETIC_LIGHTS_ON = True
    
def launch_background_lights(step):
    global previous_step
    if(previous_step == step):
        return
    instructions = get_background_lights(step)
    if instructions == None:
        previous_step = step
        return
    print('read instructions')
    instructions = read_file(BACKGROUND_LIGHTS_PATH + instructions)
    print('get background lights')
    background_light = instructions_to_lights(instructions)
    print('start background lights')
    background_light.start()
    print('continue')
    previous_step = step

    
def finish_diegetic_lights():
    global diegetic_processes
    global unfinished_transitions
    global DIEGETIC_LIGHTS_ON
    for process in diegetic_processes:
        process.join()
        utils.sleep(1)
    diegetic_processes = []
    for transition in unfinished_transitions:
        while transition.number > 0:
            time = transition.start()
            utils.countdown(time + 1)
    unfinished_transitions = []
    DIEGETIC_LIGHTS_ON = False