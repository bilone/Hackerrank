n, m = input().split()

l1 = [int(i) for i in input().split()]
A = set([int(i) for i in input().split()])
B = set([int(i) for i in input().split()])
count = 0
for i in range(len(l1)):
    if l1[i] in A:
        count += 1
    if l1[i] in B:
        count -= 1

print(count)