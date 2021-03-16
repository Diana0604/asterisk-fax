import time, os

DEBUG = 1

def debug(message):
    if DEBUG > 0:
        print(message)

def remove_files_from(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def countdown(secs):
    while(secs > 0):
        time.sleep(1)
        print(secs)
        secs = secs - 1

def check_for_wifi():
    stream = os.popen("ifconfig wlan0")
    time.sleep(1)
    output = stream.read()
    if output.find("inet") == -1:
        print('RECONNECTING')
        os.popen("wpa_cli -i wlan0 reconfigure")

def send_email(message, subject = 'GENERIC'):
    message = message + ' '
    os.system("sendemail -f diana.valverdu@gmail.com -t helpline.wsf.2@gmail.com -u '" + subject + "' -m '" + message + "' -xu diana.vallverdu@gmail.com -xp fcnxcntclkxrrxvd -s smtp.gmail.com")