student_score = input("Input a list of student scores ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
count = 0
highest = 0
for i in student_score:
    count = count + 1

for j in range(0, count):
    if highest < student_score[j]:
        highest = student_score[j]

print(f"The highest score in the class is: {highest}")
