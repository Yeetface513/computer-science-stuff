from hashlib import sha256
import sys
import random as chez
import operator

# input_username = input('Enter your username: ')
# input_password = input('Enter your password: ')

#realpassword = '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
#realusername = 'f8f9499247f3ac404137af5c19d38c547ea82e331f26942cc9862895f4b09f80'

#amogus = (sha256(input_username.encode('utf-8')).hexdigest())
#fortnite = (sha256(input_password.encode('utf-8')).hexdigest())

# if amogus == realusername and fortnite == realpassword:
 #   input_username = ''
  #  input_password = ''
   # amogus = ''
 #   fortnite = ''
#else:
 #   print("that is not correct!")
  #  sys.exit()

ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}

print("Time secure maths!")
cheese = chez.randint(1,100)
fortnite = chez.randint(1,100)
operators = ['+','-','*','/']
pubg = chez.choice(operators)
answer = ops.get(op)(cheese,fortnite)
userInput = int(input(f"what is the answer to {cheese,pubg,fortnite}"))
if userInput == answer:
    print("yay")
else:
    print("rip bozo bad")
print(answer)