# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:05:27 2020

@author: Zepeda
"""

# Exercise 2 #

#Exercise 2: Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this look for lines
#that start with “From”, then look for the third word and keep a running
#count of each of the days of the week. At the end of the program print
#out the contents of your dictionary (order does not matter).



while True:
    fname = input('Enter a file:')
    try:
        handle = open(fname)
    except:
        print('Enter a valid file!')
        continue
    break

dweek = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        print(words)
        dweek[words[2]] = dweek.get(words[2],0) + 1

print(dweek)

