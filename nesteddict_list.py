#dict in list
def add_new(name,roll_no,age,course) :
   new_student = {}
   new_student["Name"] = name
   new_student["roll_no"] = roll_no
   new_student["age"] = age
   new_student["course"] = course
   student_data.append(new_student)

student_data = [
   {"Name" : "Ram" , 
    "roll_no" : 10 ,
    "age" : 20,
    "course" : "Java"
   } ,
   {"Name" : "Shyam" , 
    "roll_no" : 20 ,
    "age" : 22,
    "course" :"Python"
   }
]
#print(student_data)

add_new("Mohan" , 22, 25, "C")
print(student_data)
