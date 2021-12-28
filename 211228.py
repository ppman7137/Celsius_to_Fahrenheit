# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 23:54:00 2021

@author: user
"""

age = input('請輸入年齡: ')
age = float(age)
if age >= 20:
    print('can vote')

degree_C = input('please input your body temperature in Celsius: ')
degree_C = float(degree_C)
degree_F = degree_C * 9 / 5 + 32
print('degree in Fahrenheit is:',degree_F) 
