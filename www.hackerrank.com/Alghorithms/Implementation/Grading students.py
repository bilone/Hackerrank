"""
HackerLand University has the following grading policy:

Every student receives a  grade in the inclusive range from  0 to 100 .
Any  less than 40  is a failing grade.
Sam is a professor at the university and likes to round each student's grade  according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round  grade up to the next multiple of 5 .
If the value grade of  is less than 38 , no rounding occurs as the result will still be a failing grade.
For example, grade=84  will be rounded to 85 but grade=29  will not be rounded because the rounding would result in a number that is less
than .
Given the initial value of  for each of Sam's  students, write code to automate the rounding process. For each , round
it according to the rules above and print the result on a new line.
"""

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        k=5-(grades[i]%5)
        if grades[i]>=38:
            if k<3:
                grades[i]=grades[i]+k

    return(grades)

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
