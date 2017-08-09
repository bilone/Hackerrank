n=int(input())
setA=set(map(int,input().split()))
s=[]
N=int(input())
for i in range(N):
    cmd,k=input().split()
    s=set(map(int,input().split()))
    if cmd=='update':
        setA.update(s)
        print(setA)
    elif cmd=='intersection_update':
        setA.intersection_update(s)
        print(setA)
    elif cmd=='difference_update':
        setA.difference_update(s)
        print(setA)
    elif cmd=='symmetric_difference_update':
        setA.symmetric_difference_update(s)
        print(setA)
print(sum(setA))