def count_substring(string, sub_string):
    l=[]
    for i in range(len(string)):
        k=string.find(sub_string,i)
        if k!=-1:
            l.append(k)
    s1=set(l)
    return len(s1)

string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)
count=0
