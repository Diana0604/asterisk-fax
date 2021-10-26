import sys
sys.path.insert(1, '/fax/python')
import smoke

smoke.start_smoke()

question = raw_input("Write OK if you see smoke. Write anything else otherwise. ")


if question != "OK":
    print('ERROR => SMOKE FAILED!')
    sys.exit()


print('======================================= CALLS - SUCCESS! ============================')