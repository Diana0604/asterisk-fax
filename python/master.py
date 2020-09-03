#imports
import manager, debug

#helpers
debugger = debug.Debug(1)

def invalid_step():
    debugger.title('INVALID STEP')

def get_option(var):
    try: 
        int(var)
        return int(var)
    except ValueError:
        return 0

#vars
ended = False

manager.override_reboot()

def switch_steps(i):
    switcher = {
        1: manager.step1_healthcall,
        2: manager.step2_healthfax1,
        3: manager.step3_healthfax2,
        4: manager.step4_helloworld,
        5: manager.step5_trust1,
        6: manager.step6_trust2,
        7: manager.step7_trust3,
        8: manager.step8_antenna,
        9: manager.step9_spies,
        10: manager.step10_mission,
        11: manager.step11_consignia,
        12: manager.step12_laststeps_explained,
        13: manager.step13_laststeps,
        100: manager.exit
    }
    func=switcher.get(i, invalid_step)
    return func()

while not ended :
    debugger.title("WELCOME TO THE FAX CONTROLLER")
    debugger.title("THESE ARE THE POSSIBLE STEPS: ")
    debugger.subtitle("HEALTHCHECKS")
    debugger.log("[1] -> healthcheck number 1. This is the first call that is launched on the show.")
    debugger.log("[2] -> healthcheck number 2. This is the first fax that is launched. You should launch this option after ~30 seconds of first step.")
    debugger.log("[3] -> Ending of healthchecks. This is launched after they have BOTH made a call and sent us a fax. Fax is the last thing that happens.")
    debugger.log("[3] -> Ending of healthchecks. This is launched after they have BOTH made a call and sent us a fax. Fax is the last thing that happens.")
    debugger.subtitle("HELLO WORLD + TRUST EXERCISES")
    debugger.log("[4] -> helloworld fax. This fax is sent after all the healthchecks have been made. Wait a bit after healthcheck 3 to launch it. It marks the beginning of the show.")
    debugger.log("[5] -> trust exercise 1. This goes after they have sent us the checklist with everything done.")
    debugger.log("[6] -> trust exercise 2. This goes after they have called 126.")
    debugger.log("[7] -> trust exercise 3. This goes after they have called 1999.")
    debugger.subtitle("ANTENNA / SPIES / MISSION")
    debugger.log("[8] -> antenna. This goes after they have sent us their questionnaire answers.")
    debugger.log("[9] -> spies. This goes after they have called they have called 555.")
    debugger.log("[10] -> mission. This goes after they have called they have called 42.")
    debugger.subtitle("CONSIGNIA")
    debugger.log("[11] -> consignia fax. This goes after they have sent back their allergies.")
    debugger.subtitle("FINAL STEPS")
    debugger.log("[12] -> final steps explanation. Launch the fax with the final steps explaines. We will be on the phone (hopefully). Send it when appropriate.")
    debugger.log("[13] -> final steps. We will be on the phone (hopefully). Send it when appropriate. This launches the preprogrammed ending (nothing to do from now on!). ")
    option = get_option(raw_input("LET ME KNOW WHAT STEP ARE YOU ON (I only need the number): "))
    debugger.blank_lines() 
    switch_steps(option)
    if option == 100:
        ended = True
    debugger.blank_lines()

