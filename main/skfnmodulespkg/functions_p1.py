student = {"name":"satish", "student_age": 34, "course":"math"}

def update_name(new_name, new_course):
    student["name"] = new_name
    student["course"] = new_course

# # def update_name(new_name, student_dict):
# #     student_dict["name"] = new_name
# #     return student_dict

# def update_name(new_name):
#     student["name"] = new_name

update_name("meer2", "ml")

student[1] = "roll_number1"

print("Modified Student details are: ", student)

student[1] = "roll_number2"

print("Modified Student roll number is: ", student[1])

# add numbers
# def add_num(num1, num2, num3=0):
#     added_result = num1+num2+num3
#     return added_result

# print(f"Sum of all these is: ", add_num(1,2))

# def add_num(num1, num2, num3=0, avg=False):
#     print(f"input are: num1: {num1}, num2: {num2},num3: {num3} and avg: {avg}")
#     added_result = num1+num2+num3
#     if avg == True:
#         print("Average is : ", added_result/3)
#     return added_result

# print(f"Sum of all these is: ", add_num(num2=2, num1=1,avg=True))

# print(f"Sum of all these is: ", add_num(2, 1,True)) # it is coverting true to 1 and adding it

# print(f"Sum of all these is: ", add_num(2, 1,avg=True))


# if __name__ == "__main__":
#     print(f"Sum of all these is: ", add_num(num2=2, num1=1,avg=True))

#     print(f"Sum of all these is: ", add_num(2, 1,True)) # it is coverting true to 1 and adding it

#     print(f"Sum of all these is: ", add_num(2, 1,avg=True))
    
#     print("Student details are: ", student)
#     update_name("meer2")
#     print("Modified Student details are: ", student)
