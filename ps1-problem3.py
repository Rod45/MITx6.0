# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:54:42 2016

@author: Rod Lewis
Instructions:
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a break and cleared your head.

"""
s = 'abcbcd'
temp = s[0]
subString = s[0]
length = len(s)
for i in range(1, length):
    if s[i] >= temp[-1]:
        temp += s[i]
        if len(temp) > len(subString):
            subString = temp
    else:
        temp = s[i]

print('Longest substring in alphabetical order is:' + subString)