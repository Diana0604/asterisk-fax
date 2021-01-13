from gpiozero import LED
from time import sleep
import utils

led = LED(26)

charger = LED(5)
charger.on()

current_step = None

led.off()

def start_smoke():
    charger.off()
    led.on()
    sleep(10)
    led.off()
    charger.on()

def launch_smoke(step):
    global current_step
    if(step == current_step):
        return False
    if step == '25':
        utils.debug('smoke')
        start_smoke()
        current_step = step
        return True
    current_step = step
    return False
