#from gpiozero import PWMLED
from gpiozero import RGBLED
#led = RGBLED(2, 3, 4)
from time import sleep
import os, utils
Red = 17
Green = 27
Blue = 22

led = RGBLED(Red, Green, Blue)


LIGHTS_PATH = '/fax/lights/'
DIEGETIC_LIGHTS_PATH = LIGHTS_PATH + 'diegetic/'
BACKGROUND_LIGHTS_PATH = LIGHTS_PATH + 'background/'
background_lights = os.listdir(BACKGROUND_LIGHTS_PATH)
diegetic_lights = os.listdir(DIEGETIC_LIGHTS_PATH)

DIEGETIC_LIGHTS_ON = False

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
    print(previous_step)
    print(step)
    if(previous_step == step):
        return False
    lights_file = get_diegetic_lights(step)
    if lights_file == None:
        return False
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
        process = Process(target=utils.countdown, args=(int(instructions[7]),))
        process.start()
        diegetic_processes.append(process)
    if instructions[0] == 'blink':
        print('blinking')
        blink_red = float(instructions[1])
        blink_green = float(instructions[2])
        blink_blue = float(instructions[3])
        n = int(instructions[4])
        led.blink(on_time=3, off_time=1, fade_in_time=0, fade_out_time=0, on_color=(blink_red, blink_green, blink_blue), off_color=led.color, n=n, background=True)
        process = Process(target=utils.countdown, args=(4*n,))
        process.start()
        diegetic_processes.append(process)
    if instructions[0] == 'twinkle':
        print('blinking')
        on_red = float(instructions[1])
        on_green = float(instructions[2])
        on_blue = float(instructions[3])
        off_red = float(instructions[4])
        off_green = float(instructions[5])
        off_blue = float(instructions[6])
        n = int(instructions[7])
        led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0, on_color=(on_red, on_green, on_blue), off_color=(off_red, off_green, off_blue), n=n, background=True)
        process = Process(target=utils.countdown, args=(2*n,))
        process.start()
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
    instructions = read_file(BACKGROUND_LIGHTS_PATH + instructions)
    if instructions[0] == 'pulse':
        print('pulsating')
        on_color = float(instructions[1]), float(instructions[2]), float(instructions[3])
        led.pulse(fade_in_time=10, fade_out_time=10, on_color=on_color, off_color=(0.1, 0.1, 0.1), n=None, background=True)
    else :
        led.color = (float(instructions[0]), float(instructions[1]), float(instructions[2]))
    previous_step = step
    print('previous_step ' + previous_step)
    print('step' + step)

    
def finish_diegetic_lights():
    global diegetic_processes
    global DIEGETIC_LIGHTS_ON
    for process in diegetic_processes:
        process.join()
    diegetic_processes = []
    DIEGETIC_LIGHTS_ON = False