import sys
sys.path.insert(1, '/fax/python')
import sounds


sound = '/fax/sounds/speaker/pre_show_message.wav'
sounds.play_sound(sound)


question = raw_input("Write OK if you can hear Diana and Zhaolin telling you off. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => SOUND NOT PLAYING!')
    sys.exit()


print('======================================= SOUNDS - SUCCESS! ============================')