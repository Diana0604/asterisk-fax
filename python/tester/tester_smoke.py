import sys
sys.path.insert(1, '/fax/python')
import smoke

smoke.start_smoke()

from signal import pause

question = raw_input("Write OK if you saw smoke. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => SMOKE FAILED!')
    sys.exit()


print('======================================= SMOKE - SUCCESS! ============================')