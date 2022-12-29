grades = list()
for i in range(5):
  grade = int(input())
  if grade >= 40:
    grades.append(grade)
  else:
    grades.append(40)

print(sum(grades)//5)