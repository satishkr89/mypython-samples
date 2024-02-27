#student_data = open("/Users/satishkumar/Library/CloudStorage/Dropbox/Mac/Downloads/Student_data.txt")
student_data = open("/Users/satishkumar/Library/CloudStorage/Dropbox/Mac/Downloads/new_student_data.txt")

students = student_data.readlines()
# for student in students:
#    student = student.strip()
#    print(f"Student {student}")
students_dict={}

# for i in range(0, len(students), 5):
#    student = students[i].strip()
#    subject1 = students[i+1].strip()
#    subject1_and_marks = subject1.split()
#    subject2 = students[i+2].strip()
#    subject2_and_marks = subject2.split()
#    subject3 = students[i+3].strip()
#    subject3_and_marks = subject3.split()
#    print(f"Student {student}, subjects and marks are: {subject1}, {subject2}, {subject3}")

#    print(f"Student {student}, subjects and marks are: {subject1_and_marks}, {subject2_and_marks}, {subject3_and_marks}")
#    print("-----------------")
   
#    students_dict[student] = {subject1_and_marks[0]:int(subject1_and_marks[1]), 
#                                subject2_and_marks[0]:int(subject2_and_marks[1]), 
#                                subject3_and_marks[0]:int(subject3_and_marks[1])}
   
#    #print("-------dictionary----------", students_dict)

# print("-------dictionary----------", students_dict)


for i in range(0, len(students), 5):
   student = students[i].strip().replace(":","")
   subject1 = students[i+1].strip().replace(":","")
   subject1_and_marks = subject1.split()
   subject2 = students[i+2].strip().replace(":","")
   subject2_and_marks = subject2.split()
   subject3 = students[i+3].strip().replace(":","")
   subject3_and_marks = subject3.split()
   print(f"Student {student}, subjects and marks are: {subject1}, {subject2}, {subject3}")

   print(f"Student {student}, subjects and marks are: {subject1_and_marks}, {subject2_and_marks}, {subject3_and_marks}")
   print("-----------------")
   
   students_dict[student] = {subject1_and_marks[0]:int(subject1_and_marks[1]), 
                               subject2_and_marks[0]:int(subject2_and_marks[1]), 
                               subject3_and_marks[0]:int(subject3_and_marks[1])}
   
   #print("-------dictionary----------", students_dict)

print("-------dictionary----------", students_dict)
student_data.close()
