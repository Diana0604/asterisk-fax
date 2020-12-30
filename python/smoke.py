from gpiozero import LED
from time import sleep

led = LED(26)

current_step = None

led.off()

def start_smoke():
    led.on()
    sleep(10)
    led.off()

def launch_smoke(step):
    global current_step
    if(step == current_step):
        return False
    if step == '25':
        print('smoke')
        start_smoke()
        current_step = step
        return True
    current_step = step
    return False