#!/bin/python3

import sys


S = input().strip()
t=len(S)
m=t//3
S1=m*'SOS'
count=0
for i in range(t):
    if S[i]!=S1[i]:
        count+=1
print(count)