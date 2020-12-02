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
    print('step')
    global current_step
    if(step == current_step):
        return
    if step == '24':
        print('smoke')
        start_smoke()
    current_step = step