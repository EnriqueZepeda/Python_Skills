# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:38:10 2020

@author: Zepeda
"""

# Excercise 8.1 #

# Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
def chop(t):
    t.pop(0)
    t.pop(len(t)-1)
    return None

t1 = [1,2,3,4,5]
t2 = [1,2,3,4,5]

chop(t1)

print(t1)

def middle(t):
    x = t[1:len(t)-1]
#    print(x is t)
    return x

print(middle(t2))
print(t2)
