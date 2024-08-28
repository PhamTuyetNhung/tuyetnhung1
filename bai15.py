# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:17:55 2024

@author: Nhung Pham
"""
a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
A=((a+b)/(a**(1/3)+b**(1/3))) - ((a*b)**(1/3))
B=((a**(1/3))-(b**(1/3)))**2 
print("Kết quả là:", A/B)