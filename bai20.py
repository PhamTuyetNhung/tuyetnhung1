# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:07:01 2024

@author: Nhung Pham
"""
a=int(input("Nhập vào số nguyên a:"))
b=int(input("Nhập vào số nguyên b:"))
c=int(input("Nhập vào số nguyên c:"))
if a>b and a>c:
    print("Số lớn nhất là:",a)
elif b>a and b>c:
    print("Số lớn nhất là:",b)
else:
    print("Số lớn nhất là:",c)
