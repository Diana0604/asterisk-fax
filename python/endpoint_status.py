# Program to run "asterisk -rx 'pjsip list endpoints'" and check status of endpoinds
import os

#print(splited_output)

def fax_free():
    stream = os.popen("asterisk -rx 'pjsip list endpoints'")
    output = stream.read()
    splited_output = output.split()
    i = 0
    while i < len(splited_output):
        element = splited_output[i]
        if element == '1000/1000':
            element_info = splited_output[i+1]
            if element_info == 'Not':
                return True
            else:
                return False
        i = i + 1