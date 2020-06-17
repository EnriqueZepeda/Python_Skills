# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:46:19 2020

@author: Zepeda
"""

numbers = []

while True:
    number = input('Enter a number:')
    if number == 'done':
        break
    try:
       number = float(number);
    except:
        print('Error, not a valid number')
        continue
    numbers.append(number)

print(numbers)
print('Max:',max(numbers))
print('Min:',min(numbers))
    