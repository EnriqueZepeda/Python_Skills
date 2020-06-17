# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:54:44 2020

@author: Zepeda
"""

# Exercise 9_1 #

import string

# Asking user for a valid file to read
q = 0 # bandera de salida de emergencia

while True:
    fname = input('Enter a file:')
    if fname == 'done':
        q = 1
        break
    try:
        handle = open(fname)
    except:
        print('Error! Invalid file name')
        continue
    break

if q == 1:
    exit()

histogram = dict()
bigword = None
bigcount = None
      
# Reading the text, making histogram
for line in handle:
    line = line.translate(line.maketrans('','',string.punctuation))
    words = line.split()
    for i in words:
        i = i.lower()
        histogram[i] = histogram.get(i,0) + 1
#        if i in histogram:
#            histogram[i] = histogram[i] + 1
#        else:
#            histogram[i] = 1

# print(histogram)

# Ask for a particular word in the text, returns number of times it appears.
while True:
    wrdasked = input('Enter a word:')
   
    # Guardian (not necessary I guess)
    try:
        wrdasked = wrdasked.lower()
    except:
        print('Enter a word')
        continue
    
    if wrdasked == 'done':
        break
    elif wrdasked in histogram:
        print(wrdasked, 'is in', fname, histogram[wrdasked], 'times.')
        continue
    else:
        print(wrdasked, 'does not appear in', fname + '!')
        continue
    
print(histogram,'\n')

val = histogram.values()

bigcount = max(val)

for key in histogram:
    if histogram[key] == bigcount:
        bigword = key

print('\"' + bigword + '\"','appears', bigcount, 'times in the file.')

#for aaa,bbb in histogram:
#    print(aaa,bbb)
#    if bbb > bigcount:
#        bigcount = bbb
#        bigword = aaa
#
#print(bigword, bigcount)
    
        