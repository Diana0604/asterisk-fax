from gpiozero import Button
import os, asterisk

#reboot
reboot_button = Button(23)
def reboot():
    os.system('reboot')
    print('rebooting')
reboot_button.when_pressed = reboot

#rescue
rescue_button = Button(24)
def rescue():
    os.system('tmate -S /tmp/tmate.sock new-session -d')
    # Blocks until the SSH connection is established
    os.system('tmate -S /tmp/tmate.sock wait tmate-ready')
    #get web session
    stream = os.popen("tmate -S /tmp/tmate.sock display -p '#{tmate_web}' ")
    #print(stream)
    output = stream.readline()
    print(output)
    os.system("sendemail -f diana.valverdu@gmail.com -t diana.vallverdu@gmail.com -u 'RESCUE SESSION' -m 'RESCUE SESSION " + output + "' -xu diana.vallverdu@gmail.com -xp fcnxcntclkxrrxvd -s smtp.gmail.com")

rescue_button.when_pressed = rescue

wormhole_button = Button(16)

def wormhole():
    print('wormhole')
    asterisk.add_to_database('step', '25')

wormhole_button.when_pressed = wormhole