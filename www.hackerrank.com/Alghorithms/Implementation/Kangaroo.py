import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    res='NO'
    if x2>x1 and v2<v1:
        if abs(x1-x2)%abs(v1-v2)==0:
            res='YES'
    return(res)
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
