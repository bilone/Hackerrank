import sys

def getRecord(s):
    # Complete this function
    Rmax=s[0]
    cmax=0
    Rmin=s[0]
    cmin=0
    for i in range(len(s)):
        if s[i]>Rmax:
            Rmax=s[i]
            cmax+=1
        if s[i]<Rmin:
            Rmin=s[i]
            cmin+=1
    return(cmax,cmin)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))