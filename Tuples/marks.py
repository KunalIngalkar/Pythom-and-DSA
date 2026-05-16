mixed_marks = [('A', 80), ('B', 95), ('C', 85)]

for i in range(len(mixed_marks)):
    for j in range (i + 1, len(mixed_marks)):
        if mixed_marks[i][1] < mixed_marks[j][1]:
            mixed_marks[i], mixed_marks[j] = mixed_marks[j], mixed_marks[i]
print(mixed_marks)