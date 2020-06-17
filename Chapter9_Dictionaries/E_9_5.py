# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:29:17 2020

@author: Zepeda
"""

#Exercise 5: This program records the domain name (instead of the
#address) where the message was sent from instead of who the mail came
#from (i.e., the whole email address). At the end of the program, print
#out the contents of your dictionary.

while True:
    fname = input('Enter a file:')
    if fname == '1':
        fname = 'mbox-short.txt'
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
    for item in words:
        if '@' in item:
            pos = item.find('@')
            words[1] = item[(pos + 1):]
    if len(words) > 0 and words[0] == 'From':
        #print(words)
        d[words[1]] = d.get(words[1],0) + 1

print(d)

print(d.get('h',-1))
