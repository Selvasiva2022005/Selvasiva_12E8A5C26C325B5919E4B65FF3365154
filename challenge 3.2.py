class Student:
   def __init__(self,name,roll_number,cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa
def sort_students(student_list):
   sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
   return sorted_students

students = [
  Student("Selvasiva","A123",9.4),
  Student("Christina Joy","A124",8.3),
  Student("Tharunya","A125",7.2),
  Student("Saranya","A126",9.9),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll_number: {}, CGPA:{}".format(student.name,student.roll_number,student.cgpa))