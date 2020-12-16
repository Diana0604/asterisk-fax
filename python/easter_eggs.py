import asterisk
def start_easter_eggs():
    egg = 'egg'
    for egg_number in range(1, 25):
        new_egg = egg + str(egg_number)
        asterisk.add_to_database(new_egg, "NO")
        new_egg = egg + str(egg_number)

def get_easter_egg_sound(egg_number):
    if egg_number == 1:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_1_countdown.wav'
    if egg_number == 2:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_2_potatoes.wav'
    if egg_number == 3:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_3_feast.wav'
    if egg_number == 4:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_4_terraform.wav'
    if egg_number == 5:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_5_hopeless.wav'
    if egg_number == 6:
        return '/fax/sounds/speaker/phone_call/08_achieve_levelone.wav'
    if egg_number == 7:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_7_errormessage.wav'
    if egg_number == 23:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_23_errormessage.wav'
    if egg_number == 24:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_24_errormessage.wav'
    if egg_number == 9:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_9_Birthday.wav'
    if egg_number == 11:
        return '/fax/sounds/speaker/phone_call/08_achieve_levelone.wav'