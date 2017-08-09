students=[]
scores=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    scores.append(score)

m1=min(scores)
m2= min([scores[i] for i in range(len(scores))  if scores[i]!=m1])
temp=[students[i][0] for i in range(len(students)) if students[i][1]==m2]
print(temp)
temp.sort()
for i in range(len(temp)):
    print(temp[i])
