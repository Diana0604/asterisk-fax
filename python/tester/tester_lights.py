import sys, version
sys.path.insert(1, '/fax/python')
import lights

question = version.get_input("Write OK if you see nothing. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => LIGHTS NOT OFF WHEN THEY SHOULD BE OFF')
    sys.exit()

lights.instructions_to_lights(['constant','color',1,0,0]).start()

question = version.get_input("Write OK if you see red. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => LIGHTS NOT TURNING RED!')
    sys.exit()

lights.instructions_to_lights(['constant','color',0,1,0]).start()

question = version.get_input("Write OK if you see green. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => LIGHTS NOT TURNING GREEN!')
    sys.exit()

lights.instructions_to_lights(['constant','color',0,0,1]).start()

question = version.get_input("Write OK if you see blue. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => LIGHTS NOT TURNING BLUE!')
    sys.exit()

print('======================================= LIGHTS - SUCCESS! ============================')