# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:13:44 2020

@author: Zepeda
"""

# E_2 #

fname = input('Enter file name:');

try:
    text = open(fname);
except:
    print('Error! Please enter a valid file name:');
    quit();

count = 0;

for line in text:
    line = line.rstrip();
    if not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split();
    print(words[1]);
    count = count + 1;
    
print("There were", count, "lines in the file with From as the first word")