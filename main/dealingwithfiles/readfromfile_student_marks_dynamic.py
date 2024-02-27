from pprint import pprint

#student_data = open("/Users/satishkumar/Development/python-projects/Student_data.txt")
student_data = open("/Users/satishkumar/Development/python-projects/more_student_data-1.txt")


all_students_data = student_data.readlines()
# print(f"all student data: {all_students_data}")

#num_subject = int(input("How many subjects each student got marks for? :"))
num_subject = all_students_data.index("\n")
students_dict={}

#find index of empty line 

for i in range(0, len(all_students_data), num_subject+1):
   student_name = all_students_data[i].strip().replace(":","")
   #print(f"For student {student_name}")
   subject_dict={}
   for num_of_sub_counter in range(i+1, i+num_subject): # i in this line is to skip name line
      subject_marks = all_students_data[num_of_sub_counter].strip().replace(":","")
      subject_marks = subject_marks.split()
      #print(f"subjects and marks are:{subject_marks}")
      subject_dict[subject_marks[0]] = int(subject_marks[1])
   #print(f" subject dict: {subject_dict}")
   students_dict[student_name] = subject_dict # Aadd dict of marks to student dict
#print("-------dictionary----------", students_dict)

pprint(students_dict)

student_data.close()
