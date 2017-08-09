import sys


def solve(n, s, d, m):

    # Complete this function
    def sum(list):
        res=0
        for i in range(len(list)):
            res+=list[i]
        return(res)
    l=[]
    

    if m>1:
        count = 0

        for i in range(n-m+1):
            l.insert(i,s[i:i+m])
        for i in range(len(l)):
            if sum(l[i])==d:
                count+=1

    else:
        count=1
    print(l)

    return(count)



n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)