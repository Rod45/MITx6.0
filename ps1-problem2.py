# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:57:42 2016

@author: rod

Description:
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
s = 'azcbobobegghakl'
count = 0
bob = 'bob'
length = len(s)
for i in range(length):
    if bob in s[i:(i + 3)]:
        count += 1
print("Number of times bob occurs is: " + str(count))

