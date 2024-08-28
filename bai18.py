# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:35:55 2024

@author: Nhung Pham
"""
from datetime import timedelta 
gio1=int(input("Giờ đầu:"))
phut1=int(input("Phút đầu:"))
giay1=int(input("Giây đầu:"))
gio2=int(input("giờ thứ 2:"))
phut2=int(input("phút thứ 2:"))
giay2=int(input("giây thứ 2:"))
time1=timedelta(seconds=giay1,minutes=phut1,hours=gio1)
time2=timedelta(seconds=giay2,minutes=phut2,hours=gio2)
time3=time1+time2
time4=time1-time2
print("Kết quả:",time3)
print("Kết quả:",time4)
    
    
    
