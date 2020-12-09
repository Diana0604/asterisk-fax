import asterisk, calls, sounds
import time

def check_easter_eggs():
    egg = 'egg'
    egg_number = 1
    new_egg = egg + str(egg_number)
    while asterisk.database_exists(new_egg):
        print('testing egg: ' + new_egg)
        print(asterisk.get_from_database(new_egg))
        if  asterisk.get_from_database(new_egg) == "YES":
            print('found egg' + str(egg_number))
            execute_egg(egg_number)
            asterisk.add_to_database(new_egg, "NO")
        egg_number = egg_number + 1
        new_egg = egg + str(egg_number)

def execute_egg(egg_number):
    print('executing egg ' + str(egg_number))
    print(egg_number)
    if egg_number == 1:
        print('executing egg 1')
        calls.launch_call('tester.call')
        calls.finish_call('tester.call')
    if egg_number == 2:
        sounds.play_sound('/fax/sounds/speaker/phone_call/08_achieve_levelone.wav', False)