marks = list(input("Введите оценки: "))
total_marks = 0
for i in marks:
    if i != "2":
        total_marks += 1
progress = (total_marks / len(marks)) * 100
print(len(marks), progress, marks)
