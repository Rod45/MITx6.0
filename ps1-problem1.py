# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 16:00:22 2016

@author: rod

Description:
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""
s = 'azcbobobegghakl'
count = 0
x = s.lower()
vowels = {"a", "e", "i", "o", "u"}
for letter in x:
    if letter in vowels:
        count +=1
print("Number of vowels: " + str(count))