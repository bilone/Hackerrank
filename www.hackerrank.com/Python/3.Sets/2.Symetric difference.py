N1=int(input())
l1=list(map(int,input().split()))
N2=int(input())
l2=list(map(int,input().split()))
s1=set(l1)
s2=set(l2)
t1=list(s1.difference(s2))
t2=list(s2.difference(s1))
l2=t1+t2
l2.sort()
for i in range(len(l2)):
    print(l2[i])
