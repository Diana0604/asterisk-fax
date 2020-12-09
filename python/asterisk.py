# Program to run "asterisk -rx 'pjsip list endpoints'" and check status of endpoinds
import os, time

ASTLOGS = '/var/log/asterisk/full'
LASTLINE  = ''

#clean all residual errors
f = open(ASTLOGS, 'r')
while True:
    line = f.readline()
    if not line:
        break
    LASTLINE = line

def check_fax_status():
    stream = os.popen("asterisk -rx 'pjsip list endpoints'")
    output = stream.read()
    splited_output = output.split()
    i = 0
    while i < len(splited_output):
        element = splited_output[i]
        if element == '1000/1000':
            return splited_output[i+1]
        i = i + 1


def fax_free():
    if check_fax_status() == "Not":
        return True
    return False

def wait_for_fax_free():
    while not fax_free():
        time.sleep(1)
    if error():
        return False
    return True

def wait_for_fax_busy():
    while fax_free():
        time.sleep(1)
        if error():
            return False
    return True

def fax_ringing():
    if check_fax_status() == 'Ringing':
        return True
    return False

def wait_fax_not_ringing():
    while fax_ringing():
        time.sleep(1)
    
def get_database_value(output):
    return output.split()[1]

def check_current_step():
    database_output = os.popen("asterisk -rx 'database get WESTILLFAX step'").read()
    return get_database_value(database_output)

def update_step():
    if check_current_step() == '26':
        add_to_database('step', '27')
        return
    if check_current_step() == '25':
        add_to_database('step', '26')
        return
    if check_current_step() == '24':
        add_to_database('step', '25')
        return
    if check_current_step() == '21':
        add_to_database('step', '22')
        return
    if check_current_step() == '20':
        add_to_database('step', '21')
        return
    if check_current_step() == '19':
        add_to_database('step', '20')
        return
    if check_current_step() == '18':
        add_to_database('step', '19')
        return
    if check_current_step() == '15':
        add_to_database('step', '16')
        return
    if check_current_step() == '13':
        add_to_database('step', '14')
        return
    if check_current_step() == '01':
        add_to_database('step', '02')
        return
    if check_current_step() == '00':
        add_to_database('step', '01')
        return

def get_timings():
    call_times = {}
    for i in range(0,30):
        if i < 10:
            step = "0" + str(i)
        else:
            step = str(i)
        command = "asterisk -rx 'database get WESTILLFAX/call_time " + step + "'"
        database_output = os.popen(command).read()
        time = get_database_value(database_output)
        if time.isdigit():
            call_times[step] = int(time)
        else:
            call_times[step] = 0
    return call_times

def get_waits():
    call_wait = {}
    for i in range(0,30):
        if i < 10:
            step = "0" + str(i)
        else:
            step = str(i)
        command = "asterisk -rx 'database get WESTILLFAX/call_wait " + step + "'"
        database_output = os.popen(command).read()
        time = get_database_value(database_output)
        if time.isdigit():
            call_wait[step] = int(time)
        else:
            call_wait[step] = 15
    return call_wait

def error():
    global LASTLINE
    f = open(ASTLOGS, 'r')
    lines = f.readlines()
    i = len(lines) - 1
    next_line = lines[i]
    while next_line != LASTLINE:
        if 'Call failed to go through' in next_line:
            LASTLINE = lines[len(lines) - 1]
            return True
        i = i - 1
        next_line = lines[i]
    LASTLINE = lines[len(lines) - 1]
    return False
    #   [appropriate time] NOTICE[4247] pbx_spool.c: Call failed to go through, reason (3) Remote end Ringing
    #   [appropriate time] NOTICE[4247] pbx_spool.c: Queued call to PJSIP/1000 expired without completion after 0 attempts

def add_to_database(key, value): 
    # equivalent terminal command: 'asterisk -rx "database put WESTILLFAX key value"'
    command = "asterisk -rx 'database put WESTILLFAX " + key + " " + value + "'"
    print(command)
    os.system(command)

def get_from_database(key):
    command = "asterisk -rx 'database get WESTILLFAX " + key + "'"
    stream = os.popen(command)
    return stream.read().split()[1]

def database_exists(key):
    if get_from_database(key) == "entry":
        return False
    return True