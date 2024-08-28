# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:40:37 2024

@author: Nhung Pham
"""
gio=int(input("Nhập giờ:"))
phut=int(input("Nhập phút:"))
giay=int(input("Nhập giây:"))
if 0<=gio<=24 and 0<=phut<=60 and 0<=giay<=60:
    print("gio,phut,giay hợp lệ")
else:
    print("gio, phut, giay không hợp lệ")
