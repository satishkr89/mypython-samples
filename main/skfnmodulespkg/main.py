from functions_p1 import *

# import functions_p1 # import are modules

#from functions_p1 import add_num # note: this will import only fn and not global vars

#print(f"Sum of all these is: ", functions_p1.add_num(num2=2, num1=1,avg=True)) if you are usign file as module
print(f"Sum of all these is: ", add_num(num2=2, num1=1,avg=True))

print(f"Sum of all these is: ", add_num(2, 1,True)) # it is coverting true to 1 and adding it

print(f"Sum of all these is: ", add_num(2, 1,avg=True))

print("Student details are: ", student)
update_name("meer2") 
print("Modified Student details are: ", student)
