# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:55:24 2024

@author: Nhung Pham
"""
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
if a>b:
    temp=a
    a=b 
    b=temp
    if a>c:
        temp=a
        a=c
        c=temp
        if b>c :
            temp=b
            b=c
            c=temp
            print("Thứ tự tăng dần các số:",{a},{b},{c})
            
    