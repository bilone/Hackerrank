n = int(input())
l1 = []
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for item in student_marks.keys():
    if item == query_name:
        l1 = list(student_marks[item])

print(l1)
sum = 0
for i in range(len(l1)):
    sum = sum + l1[i]

print('%.2f' % float(sum / len(l1)))
