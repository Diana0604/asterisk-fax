class Debug(object):
    def __init__(self, mode = 0):
        self.mode = mode
    
    def log(self, message):
        if(self.mode > 0):
            print(message)