# Assign a letter grade based on a student's score. A(90-100), B(80-89), C(70-79), D(60-69), E(below 60)

student_score = 9

if student_score >= 101:
    print("Please verify your grade again")
    exit()

if student_score >= 90:
    print("A")
elif student_score >= 80:
    print("B")
elif student_score >= 70:
    print("C")
elif student_score >= 60:
    print("D")
else:
    print("E")
