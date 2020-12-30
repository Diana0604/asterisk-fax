from gpiozero import RGBLED
led = RGBLED(2, 3, 4)
led.color = (1, 1, 0)
print('yellow')
blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0, on_color=(1, 1, 0), off_color=(0, 0, 0), n=None, background=True)