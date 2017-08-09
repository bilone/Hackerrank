n=int(input())
s1=set(map(int,input().split()))
b=int(input())
s2=set(map(int,input().split()))
s=s1.symmetric_difference(s2)#s1^s2 wworks
print(len(s))