# Program to run "asterisk -rx 'pjsip list endpoints'" and check status of endpoinds
import os, time

ASTLOGS = '/var/log/asterisk/full'
LASTLINE  = ''

def set_last_line(line):
    global LASTLINE
    LASTLINE = line
def get_last_line():
    global LASTLINE
    return LASTLINE

f = open(ASTLOGS, 'r')
while True:
    line = f.readline()
    if not line:
        break
    set_last_line(line)

def fax_free():
    stream = os.popen("asterisk -rx 'pjsip list endpoints'")
    output = stream.read()
    splited_output = output.split()
    i = 0
    while i < len(splited_output):
        element = splited_output[i]
        if element == '1000/1000':
            element_info = splited_output[i+1]
            if element_info == 'Not':
                return True
            else:
                return False
        i = i + 1

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
    stream = os.popen("asterisk -rx 'pjsip list endpoints'")
    output = stream.read()
    splited_output = output.split()
    i = 0
    while i < len(splited_output):
        element = splited_output[i]
        if element == '1000/1000':
            element_info = splited_output[i+1]
            if element_info == 'Ringing':
                return True
            else:
                return False
        i = i + 1

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
    f = open(ASTLOGS, 'r')
    lines = f.readlines()
    i = len(lines) - 1
    next_line = lines[i]
    while next_line != get_last_line():
        if 'Call failed to go through' in next_line:
            set_last_line(lines[len(lines) - 1])
            return True
        i = i - 1
        next_line = lines[i]
    set_last_line(lines[len(lines) - 1])
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