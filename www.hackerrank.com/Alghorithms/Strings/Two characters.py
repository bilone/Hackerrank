import sys


s_len = int(input().strip())
s = input().strip()

setS=set(s)

def isTtype(s):
    l1=[]
    l2=[]
    res=False
    for i in range(len(s)):
        if i%2==0:
            l1.append(s[i])
        if i%2==1:
            l2.append(s[i])
    s1=set(l1)
    s2=set(l2)
    if s1!=s2 and len(s1)==len(s2)==1:
        res=True
    return(res)

set1 = {(x,y) for x in setS for y in setS if x!=y}
result=0
for c in set1:
    set2=setS.difference(c)
    s1=s
    for e in set2:
        s1=s1.replace(e,'')
    if isTtype(s1):
        res=len(s1)
        if res>result:
            result=res

print(result)


