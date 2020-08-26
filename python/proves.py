import threading, msvcrt
import sys

def readInput(caption, default, timeout = 5):
    class KeyboardThread(threading.Thread):
        def run(self):
            self.timedout = False
            self.input = ''
            while True:
                if msvcrt.kbhit():
                    chr = msvcrt.getche()
                    if ord(chr) == 13:
                        break
                    elif ord(chr) >= 32:
                        self.input += chr
                if len(self.input) == 0 and self.timedout:
                    break    


    sys.stdout.write('%s(%s):'%(caption, default));
    result = default
    it = KeyboardThread()
    it.start()
    it.join(timeout)
    it.timedout = True
    if len(it.input) > 0:
        # wait for rest of input
        it.join()
        result = it.input
    print ''  # needed to move to next line
    return result

# and some examples of usage
ans = readInput('Please type a name', 'john') 
print 'The name is %s' % ans
ans = readInput('Please enter a number', 10 ) 
print 'The number is %s' % ans 