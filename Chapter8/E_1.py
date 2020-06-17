# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:59:41 2020

@author: Zepeda
"""

# Excercise 1 #

#8.4 Open the file romeo.txt and read it line by line. For each line, 
#split the line into a list of words using the split() method. 
#The program should build a list of words. For each word on each line 
#check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.

t = []
fname = input('Enter file name:')

try:
    text = open(fname)
except:
    quit()
    
#print(text)
for line in text:
    line = line.rstrip()
#    print(line)
#    line = line.lower()
    words = line.split()
#    print(words)
    for i in words:
        if i in t:
            continue
        else:
            t.append(i)

t.sort()

print(t)