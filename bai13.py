# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:29:25 2024

@author: Student
"""
ngay=int(input("Nhập ngày sinh:"))
thang=int(input("Nhập tháng sinh:"))
nam=int(input("Nhập năm sinh:"))
namcuoi=nam%100
namcuoiformat=f"{namcuoi:02d}"
print(ngay,"/",thang,"/",nam)
print(ngay,"/",thang,"/",namcuoiformat) 
print(nam,"/",thang,"/",ngay)

