# create a list of any 5 books
# Task1: show the name of the last book in your list

my_books=["book-7","book-3","book-2", "book-9", "book-1"]

print("Last book in my_books list is: ", my_books[len(my_books)-1])

print("Last book in my_books list is: ", my_books[-1])


# Task2: sort your books in alphabetical order

my_books.sort()
print("Sorted book names in my_books list is: ", my_books)


# Task3: Check if the book 'Python for Data Science' is present in your list or not
if "Python for Data Science" in my_books:
    print("Book named \"Python for Data Science\" exists in my_books list is: ",my_books)
else:
    print("Book named \"Python for Data Science\" does not exists in my_books list is: ",my_books)
    
# now let us add book "Python for Data Science"
my_books.append("Python for Data Science")

if "Python for Data Science" in my_books:
    print("we added book named \"Python for Data Science\" and it exists in my_books list is: ",my_books)
else:
    print("Even though we added book named \"Python for Data Science\" and it still does not exists in my_books list is: ",my_books)

# -------------------------------
# save the full names of any 3 employees in a list
# Task1: show the employee names in all uppercase
emp_names=["Satish", "Sandy", "Arunesh"]
uppr_emp_names=[]
# for e_name in emp_names:
#     print(f"e_name is {e_name}")
#     indx = emp_names.index(e_name)+1
#     print(f"index of e_name is {indx}")
#     #emp_names.remove(e_name)
#     uppr_emp_names.append(e_name.upper())

for i in range(len(emp_names)):
    print(f"e_name is {emp_names[i]}")
    emp_names[i]=emp_names[i].upper()

#uppr_emp_names=emp_names # Assignment by ref, all data structures are ref , if copy is needed use copy funtion
uppr_emp_names=emp_names.copy()
uppr_emp_names.pop()

print("Emplayee names are : " , emp_names)
print("Emplayee names i upper case are : " , uppr_emp_names)

# Task2: show only the employees whose name start with letter 'a'
for e_name in emp_names:
    if e_name.startswith("A"):
        print(f"Employee {e_name}'s name starts with a")


# Task3: Remove the last employee from your list
uppr_emp_names = uppr_emp_names[:-1]
print("Last emplyee is removed form list: ", uppr_emp_names)

uppr_emp_names.pop()

print("Emplayee names are : " , emp_names)


# -------------------------------
# Ask the user to enter any number
# Task1: using the number entered by the user create a list of numbers squared upto the user entered number.
# For Example: if the user entered 5 the created list should be [1, 4, 9, 16, 25]
# show your list 

usr_num = int(input("Please enter a number: "))
print(f"You entered {usr_num} \n calculating square of evey number till your number....")
# ttl_sqr=0
# i=0
# while(i < usr_num):   
#     ttl_sqr += i**2
#     print(f"Square of {i} is {i**2} adding to toal: {ttl_sqr}")
#     i += 1

ttl_sqr=0
for i in range(usr_num):   
    ttl_sqr += i**2
    print(f"Square of {i} is {i**2} adding to toal: {ttl_sqr}")
    i += 1


# Task2: show only the even numbers from the list
# From the example above the even numbers would be: 4, 16
ttl_sqr=0
for i in range(usr_num):   
    if i % 2 == 0:
        ttl_sqr += i**2
        print(f"Square of only even {i} is {i**2} adding to toal: {ttl_sqr}")
    i += 1

# Task3: find the sum of all numbers in your list
ttl_sqr=0
for i in range(usr_num):   
    ttl_sqr += i
    print(f"Sum of all numbers {i} adding to toal: {ttl_sqr}")
    i += 1

# Task4: find the sum of last 3 numbers only from your list
my_num_lst=[0]
for i in range(usr_num):  
    i += 1 
    my_num_lst.append(i)
    print(f"Number {i} added to toal: {my_num_lst}")

print(f"Toal of all numbers in list : {sum(my_num_lst)}")

# Task5: find the average of all the numbers in your list
avg= sum(my_num_lst)/len(my_num_lst)
print(f"Average of all numbers in list : {avg}")


# -------------------------------
# ask user to enter any 5 numbers and make a list of those numbers
# Task1: remove the number '57' from the list
a_num_lst=[]
counter=0
while(counter<5):
    a_num_lst.append(int(input("Please enter {counter}] number out of 5 total you hvae enter: ")))
    counter +=1
print(f"All numbers in list : {a_num_lst}")
print("-----Removing 57 number from above list------")
print(f"All numbers in list except 57 : {a_num_lst.remove(57)}", a_num_lst)

# Task2: add number '100' at 1st index
a_num_lst.insert(0,100)
print(f"All numbers in list with 100 at first position : ", a_num_lst)

# Task3: show the final list elements excluding the last index
a_num_lst.pop(-1)
print(f"All numbers in list with except for number at last position : {a_num_lst}")