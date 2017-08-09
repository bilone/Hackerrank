import sys


def getTotalX(a, b):
    # Complete this function
    count = 0

    l=[]
    for k in range(max(a), min(b) + 1):
        test1 = True
        test2 = True
        for i in range(len(a)):
            if k % a[i] != 0:
                test1 = False

        for j in range(len(b)):
            if b[j] % k != 0:
                test2 = False

        if test1 and test2:
            l.append(k)
    

    return (len(l))


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)