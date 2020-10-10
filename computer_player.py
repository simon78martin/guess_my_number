# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:49:18 2020

@author: DARF

tries the middle between min and max to find the number of guess_my_number.GuessMachine
"""

import random
from guess_my_number1 import MIN, MAX, GuessMachine

if __name__ == "__main__":
    min = MIN
    max = MAX
    guess_machine = GuessMachine()
    while True:
        attempt = int((min + max)/2)
        result = guess_machine.guess(attempt)
        print("tried %d : %s" % (attempt, result))
        if result == 'found':
            print ("finished in %d attempts" % guess_machine.number_of_attempts)
            break
        elif result == 'too low':
            min = attempt +1
        else: 
            max = attempt -1
        