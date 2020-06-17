# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:19:16 2020

@author: Zepeda
"""

# Exercise 9_3 #

#Exercise 3: Write a program to read through a mail log, build a his-
#togram using a dictionary to count how many messages have come from
#each email address, and print the dictionary.

while True:
    fname = input('Enter a file:')
    try:
        handle = open(fname)
    except:
        print('Enter a valid file!')
        continue
    break

d = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        #print(words)
        d[words[1]] = d.get(words[1],0) + 1

print(d)