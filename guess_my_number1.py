# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:59:47 2020

@author: DARF
"""

import random

MIN = 0
MAX = 1000
 
class GuessMachine():
    """
    I have a nb in nb, guess it
    + self.number_to_guess is generated during creation of the object
    + use 'guess(num)' method to make a guess
    + I'll count the number of attempt in self.number_of_attempt
    """
    def __init__(self):
        self.number_to_guess = random.randint(MIN, MAX)
        self.number_of_attempts = 0
        
    def guess(self, num):
        self.number_of_attempts +=1
        if num < self.number_to_guess:
            return "too low"
        elif num > self.number_to_guess:
            return "too high"
        else: 
            return "found"
    
if __name__ == '__main__':
  guess_machine = GuessMachine()
  print("try to guess a number between %d and %d" % (MIN, MAX))

  while True:
    user_input = input("your guess ?")
    try:
      user_attempt = int(user_input)
      result = guess_machine.guess(user_attempt)
      if result == 'found':
        print("you could find a number i had in my mind in %d attempts" % guess_machine.number_of_attempts)
        break
      else :
        print(result)
    except ValueError:
        print("not an integer")