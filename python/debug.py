import sys, select

class Debug(object):
    def __init__(self, mode = 0):
        self.mode = mode
    
    def log(self, message):
        if(self.mode > 0):
            print(message)
        
    def checkpoint(self, message, wait = 10):
        print(message)
        i, o, e = select.select( [sys.stdin], [], [], wait )
