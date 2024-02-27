
# will not work for while loop

fixed_student_ids = [1,4,7 ]

student_ids1 = [ i for i in range(1,11)] #simple in line list iteration
print(student_ids1)

student_ids2 = [ i for i in range(1,11, 2)] # jump
print(student_ids2)

student_ids3 = [ i*i for i in range(1,11)] # Square
print(student_ids3)

student_ids4 = [ "UUID" + str(i) for i in range(1,11)] # prefix with some string
print(student_ids4)

student_ids5 = [ "UUID" + str(i) for i in range(1,11) if i in fixed_student_ids ] # only adding if present in another list 
print(student_ids5)

student_ids6 = [ "UUID" + str(i)+str(j) for i in range(1,11) for j in range(1,3) ] 

print(student_ids6)