# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 20:15:44 2024

@author: Nhung Pham
"""
import math 
hinh=input("Nhập hình:")
if hinh=="n":
    d=int(input("Nhập chiều dài:"))
    r=int(input("Nhập chiều rộng:"))
    P=(d+r)*2
    S=d*r
    print("P=",P,"và S=",S)
elif hinh=="v":
    c=int(input("Nhập cạnh:"))
    P=c*4
    S=c*c
    print("P=",P,"và S=",S)
else:
    r=int(input("Nhập bán kính:"))
    P=math.pi*2*r
    S=math.pi*(r**2)
    print("P=",P,"và S=",S)
    

        
        
    
