# Premiere methode#

# import string
# alpha = string.ascii_lowercase
#
# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))

#deuxieme methode#

def print_rangoli(size):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        temp = '-'.join(alp[size-1:abs(i):-1]+alp[abs(i):size])
        print(temp.center(4*size-3,'-'))


n = int(input())
print_rangoli(n)