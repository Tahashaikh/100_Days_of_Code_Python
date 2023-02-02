student_heights = [180, 124, 165, 173, 189, 169, 146]
count = 0
total_height = 0
for i in student_heights:
    count = count + 1

for j in range(0, count):
    total_height = total_height + student_heights[j]
print(f"Average Student height is : {round(total_height / count)}")

