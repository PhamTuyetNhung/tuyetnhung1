# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:59:55 2024

@author: Nhung Pham
"""
a=int(input("Nhập số nguyên a:"))
b=int(input("Nhập số nguyên b:"))
c=int(input("Nhập số nguyên c:"))
d=int(input("Nhập số nguyên d:"))
if a<b and a<c and a<d:
    print("số nhỏ nhất là:",a)
elif b<a and b<c and b<d:
    print("số nhỏ nhất là:",b)
elif c<a and c<b and c<d:
    print("số nhỏ nhất là:",c)
else:
    print("số nhỏ nhất là:",d)

    

