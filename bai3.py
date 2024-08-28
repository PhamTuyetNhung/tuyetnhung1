# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:52:10 2024

@author: Nhung Pham
"""

a=int(input("Nhập số nguyên dương a:"))
b=int(input("Nhập số nguyên dương b:"))
if a<0 and b<0:
    print("Số nhập không phải số nguyên dương vui lòng thử lại.")
else:
      print("Kết quả phép chia lấy phần nguyên là:",a//b)
      print("Kết quả phép chia lấy phần dư là:",a%b)