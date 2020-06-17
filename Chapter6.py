# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:50:18 2020

@author: Zepeda
"""

# Exercise 1 #
palabra = input('Escribe una palabra:')

long = len(palabra)
i = -1
while abs(i) <= long:
    print(long+i,':',palabra[i])
    i = i - 1

# Exercise 2 #
#nuevaPalabra = palabra[:]
#
#print(len(nuevaPalabra)) 

# Exercise 3 #
def count(char,word):
    counter = 0
    for letter in word:
        if letter == char:
            counter = counter + 1
    return counter

print('conteo propio:',count('e',palabra))

# Exercise 4 #
print('método conteo:',palabra.count('e'))

# Exercise 5 #
str = 'X-DSPAM-Confidence: 0.8475'

atspot = str.find(':')
print(atspot,len(str))

str2 = str[atspot+1:len(str)]
print(str2)
number = float(str2)
print(type(number),number)