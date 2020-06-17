# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:09:02 2020

@author: Zepeda
"""

fileHandle = open('words.txt');

for line in fileHandle:
    line = line.rstrip()
    print(line.upper())
