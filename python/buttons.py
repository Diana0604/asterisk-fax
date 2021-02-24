from gpiozero import Button
import os, asterisk, utils

#reboot
reboot_button = Button(23)
def reboot():
    utils.debug('rebooting')
    os.system("sendemail -f diana.valverdu@gmail.com -t helpline.wsf.3@gmail.com -u 'REBOOT SESSION' -m 'REBOOT SESSION ' -xu diana.vallverdu@gmail.com -xp fcnxcntclkxrrxvd -s smtp.gmail.com")
    utils.countdown(5)
    os.system('reboot')

reboot_button.when_pressed = reboot

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
    os.system("sendemail -f diana.valverdu@gmail.com -t helpline.wsf.3@gmail.com -u 'RESCUE SESSION' -m 'RESCUE SESSION " + output + "' -xu diana.vallverdu@gmail.com -xp fcnxcntclkxrrxvd -s smtp.gmail.com")

rescue_button.when_pressed = rescue

wormhole_button = Button(16)

wormhole_button_active = False

def launch_buttons(step):
    global wormhole_button_active
    if (step == '24' or step =='25') and not wormhole_button_active:
        wormhole_button.when_pressed = wormhole
        wormhole_button_active = True

def wormhole():
    utils.debug('wormhole')
    asterisk.add_to_database('step', '26')
