student = {"name":"satish", "student_age": 34, "course":"math"}
print("Student details are: ", student)

student["name"] = "meer"

print("Modified Student details are: ", student)

student["course"] = "ml"

print("Modified Student details are: ", student)

student.pop("student_age")

print("Removed student age  Student details are: ", student)

student["course_marks"] = 55

print("Modified Student details are: ", student)