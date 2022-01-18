# Program to run "asterisk -rx 'pjsip list endpoints'" and check status of endpoinds
import os, time
import utils

ASTLOGS = '/var/log/asterisk/full'
LASTLINE  = ''

#clean all residual errors
f = open(ASTLOGS, 'r')
while True:
    line = f.readline()
    if not line:
        break
    LASTLINE = line

#FAX STATUS

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
        utils.debug('waiting for fax free')
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
    if "Ring" in check_fax_status():
        return True
    return False


def wait_fax_ringing():
    while not fax_ringing():
        time.sleep(1)

def wait_fax_not_ringing():
    while fax_ringing():
        time.sleep(1)

def fax_available():
    availability = check_fax_status()
    if availability == 'Unavailable':
        return False
    print('availability: ' + availability)
    return True

def wait_fax_available():
    for i in range(0,10):
        time.sleep(1)
        if fax_available():
            return True
    utils.send_email('fax not available')
    return False

def call_on():
    utils.debug("we can see: ")
    utils.debug(get_from_database("call"))
    if(get_from_database("call") == "on"):
        return True
    return False

def init_call_on():
    if(get_from_database("init_call") == "on"):
        return True
    return False

def init_call_off():
    if(get_from_database("init_call") == "off"):
        return True
    return False

def call_off():
    if(get_from_database("call") == "off"):
        return True
    return False

def wait_call_on():
    while not call_on():
        time.sleep(1)
        if error():
            return False
    return True


def wait_init_call_on():
    while not init_call():
        time.sleep(1)
        if error():
            return False
    return True

def wait_init_call_off():
    while not init_call():
        time.sleep(1)
        if error():
            return False
    return True


def wait_call_off():
    while not call_off():
        time.sleep(1)
        if error():
            return False
    return True

def set_call_off():
    add_to_database("call", "off")


#DATABASE

def add_to_database(key, value): 
    # equivalent terminal command: 'asterisk -rx "database put WESTILLFAX key value"'
    command = "asterisk -rx 'database put WESTILLFAX " + key + " " + value + "'"
    utils.debug(command)
    os.system(command)

def get_from_database(key):
    command = "asterisk -rx 'database get WESTILLFAX " + key + "'"
    stream = os.popen(command)
    return stream.read().split()[1]

def database_exists(key):
    if get_from_database(key) == "entry":
        return False
    return True

def get_database_value(output):
    return output.split()[1]

def check_current_step():
    database_output = os.popen("asterisk -rx 'database get WESTILLFAX step'").read()
    return get_database_value(database_output)

def update_step(current_step):
    utils.debug('updating step: ' + check_current_step())
    if current_step == '03':
        add_to_database('step', '04')
        return
    if current_step == '02':
        add_to_database('step', '03')
        return

def add_one_to_step(current_step):
    new_step = str(int(current_step) + 1)
    if len(new_step) == 1:
        new_step = '0' + new_step
    add_to_database('step', new_step)

def error():
    global LASTLINE
    f = open(ASTLOGS, 'r')
    lines = f.readlines()
    i = len(lines) - 1
    next_line = lines[i]
    while next_line != LASTLINE:
        if 'Call failed to go through' in next_line:
            LASTLINE = lines[len(lines) - 1]
            utils.send_email('ERROR: Call failed to go through', 'ERROR')
            return True
        if 'error reading frame while generating CNG' in next_line:
            LASTLINE = lines[len(lines) - 1]
            utils.send_email('ERROR: Someone pressed STOP or picked up a fax call', 'ERROR')
            return True
        i = i - 1
        next_line = lines[i]
    LASTLINE = lines[len(lines) - 1]
    return False
    #   [appropriate time] NOTICE[4247] pbx_spool.c: Call failed to go through, reason (3) Remote end Ringing
    #   [appropriate time] NOTICE[4247] pbx_spool.c: Queued call to PJSIP/1000 expired without completion after 0 attempts

    if get_from_database(key) == "entry":
        return False
    return True

if not database_exists('step'):
    add_to_database('step', '00')

def resest_easter_eggs():
    add_to_database('faxegg11', '0')
    add_to_database('faxegg12', '0')
    add_to_database('faxegg14', '0')
    add_to_database('faxegg19', '0')
    add_to_database('faxegg22', '0')
    add_to_database('faxegg25', '0')
    add_to_database('faxegg26', '0')
    add_to_database('faxegg30', '0')
    add_to_database('faxegg32', '0')
