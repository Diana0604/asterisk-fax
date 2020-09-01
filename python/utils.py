import os
import signal
from subprocess import check_output

def get_pid(name):
    return check_output(["pidof",name])

def stop_previous_scripts():
    processes = get_pid('python').split()
    me = os.getpid()
    for pid in processes:
        if int(pid) != me:
            os.kill(int(pid), signal.SIGTERM)
