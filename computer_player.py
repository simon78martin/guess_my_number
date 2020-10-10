# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:49:18 2020

@author: DARF

try random ints to find the number of guess_my_number.GuessMachine
"""

import random
from guess_my_number1 import MIN, MAX, GuessMachine

if __name__ == "__main__":
    guess_machine = GuessMachine()
    while True:
        attempt = random.randint(MIN, MAX)
        result = guess_machine.guess(attempt)
        print("tried %d : %s" % (attempt, result))
        if result == 'found':
            print ("finished in %d attempts" % guess_machine.number_of_attempts)
            break
        