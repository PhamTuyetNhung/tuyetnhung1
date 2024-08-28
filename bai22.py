# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:15:35 2024

@author: Nhung Pham
"""
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
if a==0 and b==0:
    print("Phương trình có vô số nghiệm")
elif a==0 and b!=0 :
    print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Ngiệm của phương trình là:",x)
