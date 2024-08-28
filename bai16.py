# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:52:18 2024

@author: Student
"""
time=input("Nhập thời gian theo định dang (h/p/s):")
gio,phut,giay=map(int,time.replace("h"," ").replace("p"," ").replace("s"," ").split( ))
print("Số giây là:",gio*3600+phut*60+giay)

