import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    maxi=max(ar)
    s=0
    for i in range(len(ar)):
        if ar[i]==maxi:
            s+=1
    return(s)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)