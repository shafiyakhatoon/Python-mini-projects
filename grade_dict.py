students_marks = {
   "Ankit" : 60,
   "Vekit" : 90,
   "harry" : 70,
   "Suresh" : 68,
   "Reeta" : 77,
   "Seeta" : 40
}
grades = {}
for student in students_marks:
   marks = students_marks[student]
   if marks > 90:
      grades[student] = "A+"
   elif marks > 80:
      grades[student] = "A"
   elif marks > 70:
      grades[student] = "B+"
   elif marks > 60:
      grades[student] = "B+"
   elif marks > 50:
      grades[student] = "C"
   elif marks > 40:
      grades[student] = "D"
   else:
      grades[student] = "F"


print(grades)