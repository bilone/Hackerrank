'''
We say that a string, s , contains the word hackerrank if a subsequence of the characters in s  spell the word
hackerrank. For example, haacckkerrannkk does contain hackerrank, but haacckkerannk does not
(the characters all appear in the same order, but it's missing a second r).

More formally, let p0,p1,.....,p9  be the respective indices of h, a, c, k, e, r, r, a, n, k in string s. If
p0<p1<p2<...<p9 is true, then  s contains hackerrank.

You must answer q queries, where each query consists of a string,s . For each query, print YES on a new line
 if contains hackerrank; otherwise, print NO instead.

Input Format

The first line contains an integer denoting  (the number of queries).
Each line of the  subsequent lines contains a single string denoting .

Output Format

For each query, print YES on a new line if  contains hackerrank; otherwise, print NO instead.'''


import sys

test='hackerrank'
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    i=0
    j=0
    while i<len(s) and j<len(test):
        if s[i]==test[j]:
            j+=1
        i+=1

    if j==10:
        print('YES')
    else:
        print('NO')


