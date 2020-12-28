import asterisk

asterisk.add_to_database("soundegg","0")
asterisk.add_to_database("faxegg","0")

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
    if egg_number == 61:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_6_1_bodies.wav'
    if egg_number == 62:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_6_2_animals.wav'
    if egg_number == 63:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_6_3_hair.wav'
    if egg_number == 7:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_7_errormessage.wav'
    if egg_number == 23:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_23_errormessage.wav'
    if egg_number == 24:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_24_errormessage.wav'
    if egg_number == 8:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_8_glue.wav'
    if egg_number == 9:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_9_Birthday.wav'
    if egg_number == 11:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_11_help.wav'
    if egg_number == 13:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_13_news.wav'
    if egg_number == 14:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_14_Mars.wav'
    if egg_number == 17:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_17.wav'
    if egg_number == 18:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_18_spies.wav'
    if egg_number == 19:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_19_Dare.wav'
    if egg_number == 20:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_20_Tunertrade.wav'
    if egg_number == 21:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_21_Quacker.wav'
    if egg_number == 22:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_22_proposal.wav'
    if egg_number == 25:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_22_proposal.wav'
    if egg_number == 26:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_22_proposal.wav'
    if egg_number == 27:
        return '/fax/sounds/speaker/eastereggs/Easter_Egg_27_countdown.wav'

done_faxes = []

def get_easter_egg_call(egg_number):
    if egg_number == 11 and 11 not in done_faxes:
        return '11_disco_AI.call'
    if egg_number == 12 and 12 not in done_faxes:
        return '12_present.call'
    if egg_number == 14 and 14 not in done_faxes:
        return '14_Mars.call'
    if egg_number == 19 and 19 not in done_faxes:
        return '19_Dare.call'
    if egg_number == 22 and 22 not in done_faxes:
        return '22_proposal.call'
def call_made(egg_number):
    done_faxes.append(egg_number)