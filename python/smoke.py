from gpiozero import LED
from time import sleep

led = LED(26)

led.off()

#sleep(10)

while True:
    print('led on')
    led.on()
    sleep(5)
    print('led off')
    led.off()
    sleep(5)