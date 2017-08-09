def timeConversion(s):
    # Complete this function
    h1=(s[0]+s[1])
    mn1=s[3]+s[4]
    s1=s[6]+s[7]
    k=s[8]+s[9]
    if k=='AM':
        if h1=='12':
            h2='00'
        else :
            h2=h1
    if k=='PM':
        if h1=='12':
            h2=h1
        else :
            h2=str(int(h1)+12)
    return(h2+':'+mn1+':'+s1)

s = input().strip()
result = timeConversion(s)
print(result)