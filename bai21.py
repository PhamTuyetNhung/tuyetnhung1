# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:57:39 2024

@author: Nhung Pham
"""
numbers_dict={0:"Khong",1:"Mot",2 :"Hai",3 :"Ba",4 :"Bon",5  :"Nam",6 :"Sau",7 :"Bay",8 :"Tam",9 :"Chin"}
a=int(input("Nhập 1 số bất kỳ:"))
if 0<=a<=9:
    print(numbers_dict[a])
else:
    print("Khong doc duoc")
    

