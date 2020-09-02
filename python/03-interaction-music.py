#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

music.Audio(COUGHING).play()

while True:
    breathing = music.Audio(BREATHING).play()
