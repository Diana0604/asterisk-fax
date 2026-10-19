#include all neccessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel
import threading


class Lights :
  def __init__(self):
    self.pixels = neopixel.NeoPixel(board.D18, 30, brightness=1)
    #Initialise a strips variable, provide the GPIO Data Pin
    #utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)

  def wake_up(self):
    global waking_up
    waking_up = True
    def thread(pixels) :
      global waking_up
      while(waking_up) :
        print('waking up')
        #Below will loop until variabe x has value 35
        x = 10
        while x<29:
            
            pixels[x] = (255, 0, 0)
            pixels[x-5] = (255, 0, 100)
            pixels[x-10] = (0, 0, 255)
            #Add 1 to the counter
            x=x+1
            #Add a small time pause which will translate to 'smoothly' changing colour
            time.sleep(0.05)

        #below section is the same process as above loop just in reverse
        x = 19
        while x>0:
            pixels[x] = (255, 0, 0)
            pixels[x+5] = (255, 0, 100)
            pixels[x+10] = (0, 255, 0)
            x=x-1
            time.sleep(0.05)
    
    self.wake_up_thread = threading.Thread(target=thread, args=[self.pixels])
    self.wake_up_thread.start()
    
  def finish_lights(self):
    global waking_up
    waking_up = False
    self.wake_up_thread.join()
    self.pixels.fill((0, 0, 0))

#lights = Lights()

#lights.wake_up()