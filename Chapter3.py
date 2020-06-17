# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 00:16:12 2020

@author: Zepeda
"""

### Excesrise 1 & 2 ###
hours = input('Hours: ')
rate = input('Rate: ')
try:
    hours = float(hours)
    rate = float(rate)
except:
    print('Error! Please enter a numeric input')
    quit()
    
if hours > 40:
    pay = round(40*rate + (hours-40)*1.5*rate,2)
else:
    pay = round(hours*rate,2)

print('Pay:',pay)

### Excersise 3 ###
score = input('Score (0.0-1.0): ')
try:
    score = float(score)
except:
    print('Error! Please type a valid grade')
    quit()

if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Error, bad score')