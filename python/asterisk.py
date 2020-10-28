# Program to run "asterisk -rx 'pjsip list endpoints'" and check status of endpoinds
import os

#print(splited_output)

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

def get_database_value(output):
    return output.split()[1]

def check_current_step():
    database_output = os.popen("asterisk -rx 'database get WESTILLFAX step'").read()
    return get_database_value(database_output)

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
            call_wait[step] = 0
    return call_wait