from gpiozero import Button
import os, asterisk, utils

#reboot
reboot_button = Button(23)
def reboot():
    os.system('reboot')
    utils.debug('rebooting')
reboot_button.when_pressed = reboot
os.system("sendemail -f diana.valverdu@gmail.com -t helpline.wsf.4@gmail.com -u 'REBOOT SESSION' -m 'REBOOT SESSION " + output + "' -xu diana.vallverdu@gmail.com -xp fcnxcntclkxrrxvd -s smtp.gmail.com")

#rescue
rescue_button = Button(24)
def rescue():
    os.system('tmate -S /tmp/tmate.sock new-session -d')
    # Blocks until the SSH connection is established
    os.system('tmate -S /tmp/tmate.sock wait tmate-ready')
    #get web session
    stream = os.popen("tmate -S /tmp/tmate.sock display -p '#{tmate_web}' ")
    output = stream.readline()
    utils.debug(output)
    os.system("sendemail -f diana.valverdu@gmail.com -t helpline.wsf.4@gmail.com -u 'RESCUE SESSION' -m 'RESCUE SESSION " + output + "' -xu diana.vallverdu@gmail.com -xp fcnxcntclkxrrxvd -s smtp.gmail.com")

rescue_button.when_pressed = rescue

wormhole_button = Button(16)

def launch_buttons(step):
    if step == '24' or step =='25':
        wormhole_button.when_pressed = wormhole

def wormhole():
    utils.debug('wormhole')
    asterisk.add_to_database('step', '26')