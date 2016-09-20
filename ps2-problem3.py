# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 16:28:02 2016

@author: Rod Lewis
Description:
In short:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

"""

# Paste your code into this box
initBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
epsilon = 0.01
minPay = (high + low)/2.0
month = 0
def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance   
while abs(balance) >= epsilon:
    balance = initBalance
    month = 0
    balance = calculate(month, balance, minPay, monthlyInterestRate)
    if balance > 0:
        low = minPay
    else:
        high = minPay
    minPay = (high + low)/2.0
minPay = round(minPay,2)
print('Lowest Payment: ' + str(minPay))