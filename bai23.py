# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:29:22 2024

@author: Nhung Pham
"""
import math 
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
delta=(b**2)-(4*a*c)
if delta == 0:
    x=-b/2*a 
    print("Phương trình có nghiệm kép",x)
elif delta>0:
    x1= ((-b)+math.sqrt(delta))/2*a
    x2= ((-b)-math.sqrt(delta))/2*a
    print("Phương trình có 2 nghiệm phân biệt:",x1,"và",x2)
else:
    print("Phương trình vô nghiệm")
    
