import sys, select
import utils

class Debug(object):
    def __init__(self, mode = 0):
        self.mode = mode
    def title(self, message):
        spaces = utils.spaces(10)
        asterisks = utils.asterisks(70 - int(len(message)/2))
        print(spaces + asterisks + " " + message + " " + asterisks)
    def subtitle(self, message):
        spaces = utils.spaces(30)
        asterisks = utils.asterisks(50 - int(len(message)/2))
        print(spaces + asterisks + " " + message + " " + asterisks)
    def log(self, message):
        print(message)
    def blank_lines(self):
        print('\n')
        print('\n')
        
    def checkpoint(self, message, wait = 1800):
        print(message)
        select.select( [sys.stdin], [], [], wait )
