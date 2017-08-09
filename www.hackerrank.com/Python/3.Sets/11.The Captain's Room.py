K=int(input())
l=list(map(int,input().split()))
s=set(l)
print(s)
n=len(l)
s1=s
for elem in s:
    count=0
    for i in range(n):
        if l[i]==elem:
            count+=1
    if count==K:
        s1.discard(elem)
print(list(s1)[0])
