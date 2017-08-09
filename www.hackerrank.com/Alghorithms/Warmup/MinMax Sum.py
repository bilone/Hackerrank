import sys

arr = list(map(int, input().strip().split(' ')))
l1=arr
l1.sort()
sumMin=0
sumMax=0
for i in range(0,4):
    sumMin+=l1[i]
for i in range(len(arr)-4,len(arr)):
    sumMax+=l1[i]

print(sumMin,sumMax)