# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:14:45 2024

@author: Student
"""
def calculate_digit_root(number):
    while number >= 10:  
        number = sum(int(digit) for digit in str(number))
    return number
bienso= input("Nhập biển số: ")
total_sum = sum(int(digit) for digit in bienso if digit.isdigit())
digit_root = calculate_digit_root(total_sum)
print("Số nút của biển số là:", digit_root)

