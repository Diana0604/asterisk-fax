import os
import signal
from subprocess import check_output

#PIJERIES
def many_chars(char, counter):
    string = ""
    for i in range(counter):
        string = string + char
    return string
def spaces(counter):
        return many_chars(" ", counter)
def asterisks(counter):
        return many_chars("*", counter)

#I THINK THIS WON'T WORK NOW! BUT WELL HERE IT IS
def get_pid(name):
    if os.uname()[0] != 'Darwin':
        return check_output(["pidof",name])
    return ""

def stop_previous_scripts():
    processes = get_pid('python').split()
    me = os.getpid()
    for pid in processes:
        if int(pid) != me:
            os.kill(int(pid), signal.SIGTERM)
