import sys

test='abcdefghijklmnopqrstuvwxyz'
s='We promptly judged antique ivory buckles for the next prize'
s=s.lower()
print(s)
s1=set(s)

count=0
for e in s1:
    if e not in test:
        print(e)
        count+=1
print(count)
m=len(s1)-count
if m==26:
    print('pangram')
else:
    print('not pangram')