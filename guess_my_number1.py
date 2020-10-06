# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:59:47 2020

@author: DARF
"""

import random

MIN = 0
MAX = 1000

if __name__ == '__main__':
  number_to_guess =random.randint(MIN,MAX)
  print("try to guess a number between %d and %d" % (MIN, MAX))

  while True:
    user_input = input("your guess ?")
    try:
      user_attempt = int(user_input)
      if user_attempt == number_to_guess:
        print("you could find a number i had in my mind")
        break
      elif user_attempt < number_to_guess:
        print("too low")
      else :
        print("too high")
    except ValueError:
        print("not an integer")