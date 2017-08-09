n = int(input())
arr = map(int, input().split())
# first method
# l1=list(arr)
# m=max(l1)
# temp=[]
# for i in range(n):
#     if l1[i]!=m:
#         temp.append(l1[i])
#
# print(max(temp))
# second method
temp=list(arr)
m=max(temp)
print(max([temp[i] for i in range(len(temp)) if temp[i]!=m]))