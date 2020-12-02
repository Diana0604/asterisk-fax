#from gpiozero import PWMLED
from gpiozero import RGBLED
#led = RGBLED(2, 3, 4)
from time import sleep
import os, utils
Red = 17
Green = 22
Blue = 27

led = RGBLED(Red, Green, Blue)


LIGHTS_PATH = '/fax/lights/'
DIEGETIC_LIGHTS_PATH = LIGHTS_PATH + 'diegetic/'
BACKGROUND_LIGHTS_PATH = LIGHTS_PATH + 'background/'
BUTTON_LIGHTS_PATH = LIGHTS_PATH + 'button/'
background_lights = os.listdir(BACKGROUND_LIGHTS_PATH)
diegetic_lights = os.listdir(DIEGETIC_LIGHTS_PATH)
button_lights = os.listdir(BUTTON_LIGHTS_PATH)


led.color = (0,0,0)

previous_step = None
diegetic_processes = []

def get_diegetic_lights(step):
    if previous_step == step:
        return None
    for lights in diegetic_lights:
        if lights.startswith(step):
            print('found: ' + lights)
            return lights
    return None

def get_background_lights(step):
    for lights in background_lights:
        initial_step = lights[0] + lights[1]
        last_step = lights[3] + lights[4]
        if initial_step == step:
            return lights
    return None

def read_file(file):
    f = open(file)
    return f.read().split()

from multiprocessing import Process

def launch_diegetic_lights(lights_file):
    instructions = read_file(DIEGETIC_LIGHTS_PATH + lights_file)
    print(instructions)
    if instructions[0] == 'transition':
        print('transitioning')
        init_red = float(instructions[1])
        init_green = float(instructions[2])
        init_blue = float(instructions[3])
        final_red = float(instructions[4])
        final_green = float(instructions[5])
        final_blue = float(instructions[6])
        led.color = (1, 0, 0)
        led.pulse(fade_in_time=0, fade_out_time=int(instructions[7]), on_color=(init_red, init_green, init_blue), off_color=(final_red, final_green, final_blue), n=1, background=True)
        p = Process(target=utils.countdown, args=(int(instructions[7]),))
        p.start()
        diegetic_processes.append(p)
        
    print('TODO')

def launch_lights(step):
    global previous_step
    diegetic_lights_file = get_diegetic_lights(step)
    if diegetic_lights_file != None:
        launch_diegetic_lights(diegetic_lights_file)
    

    background_lights_file = get_background_lights(step)
    if background_lights_file != None:
        RGB = read_file(BACKGROUND_LIGHTS_PATH + background_lights_file)
        led.color = (float(RGB[0]), float(RGB[1]), float(RGB[2]))
    previous_step = step

def finish_diegetic_lights():
    global diegetic_processes
    for process in diegetic_processes:
        process.join()
    diegetic_processes = []