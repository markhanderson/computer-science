#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 10:59:57 2020

@author: markanderson
"""




# s = "azcbobobegghakl"

# v = ["a" "e" "i" "o" "u"]

# count = 0
        

# for s in v:
#     for v in s:
#         if v == s:
#             count = count + 1
# print(count)




myString=input()
default="aeiou"
count=0

for i in default:
    for j in myString:
        if i==j:
            count = count + 1
print('Number of vowels' + count)