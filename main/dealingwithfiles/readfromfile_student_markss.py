
#student_data = open("/Users/satishkumar/Development/python-projects/Student_data.txt")
student_data = open("/Users/satishkumar/Development/python-projects/more_student_data-1.txt")


students = student_data.readlines()

students_dict={}

for i in range(0, len(students), 7):
   student = students[i].strip().replace(":","")
   subject1 = students[i+1].strip().replace(":","")
   subject1_and_marks = subject1.split()
   subject2 = students[i+2].strip().replace(":","")
   subject2_and_marks = subject2.split()
   subject3 = students[i+3].strip().replace(":","")
   subject3_and_marks = subject3.split()
   
   subject4 = students[i+4].strip().replace(":","")
   subject4_and_marks = subject4.split()
   
   subject5 = students[i+5].strip().replace(":","")
   subject5_and_marks = subject5.split()
   
   print(f"Student {student}, subjects and marks are: {subject1}, {subject2}, {subject3}, {subject4}, {subject5}")

   print(f"Student {student}, subjects and marks are: {subject1_and_marks}, {subject2_and_marks}, {subject3_and_marks}, {subject4_and_marks}, {subject5_and_marks}")
   print("-----------------")
   
   students_dict[student] = {subject1_and_marks[0]:int(subject1_and_marks[1]), 
                               subject2_and_marks[0]:int(subject2_and_marks[1]), 
                               subject3_and_marks[0]:int(subject3_and_marks[1]),
                               subject4_and_marks[0]:int(subject4_and_marks[1]),
                               subject5_and_marks[0]:int(subject5_and_marks[1])}
   
   #print("-------dictionary----------", students_dict)

print("-------dictionary----------", students_dict)
student_data.close()
