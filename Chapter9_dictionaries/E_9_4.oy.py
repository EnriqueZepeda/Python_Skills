# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:22:29 2020

@author: Zepeda
"""

#Exercise 4: Add code to the above program to figure out who has the
#most messages in the file. After all the data has been read and the dic-
#tionary has been created, look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.

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

currentMax = None
currentAccount = None

for aaa, bbb in d:
    if bbb > currentMax:
        currentMax = bbb
        currentAccount = aaa