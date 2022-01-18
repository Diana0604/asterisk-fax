import random
import asterisk
list_init = False
possible_numbers = []

def init_list():
  global possible_numbers
  global list_init
  for i in range(1, int(asterisk.get_from_database('players'))):
    if(i < 10):
      possible_numbers.append('0' + str(i))
    else:
      possible_numbers.append(str(i))
  if(not list_init):
    possible_numbers.remove('01')
    possible_numbers.remove('04')
    list_init = True

def get_random_number():
  global possible_numbers
  global list_init
  #special case
  if(asterisk.check_current_step() == '03'):
    return '04'
  
  #initialize if not init or empty
  if(not list_init):
    init_list()
  if(not possible_numbers):
    init_list()

  #return random number from list
  chosen = random.choice(possible_numbers)
  possible_numbers.remove(chosen)
  return chosen
  

  
