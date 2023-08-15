students_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Score 91-100: Grade-"Outstanding"
# Score 81-90: Grade-"Exceeds Expectations"
# Score 71-80: Grade-"Acceptable"
# Score 70 or lower: Grade-"Fail"

student_grades = {}

for key in students_score:
    score = students_score[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)