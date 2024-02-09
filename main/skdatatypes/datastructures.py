# lists and arrays are same in native python

# my_items = ["bag","laptop","adaptor", 3, 25.5]
# print(my_items)

# print("length of my items: ", len(my_items))

# for i in range (len(my_items)):
#     print(f"counter i is : {i} item at i is {my_items[i]}")

# for item in my_items:
#     print(f"item in list is {item}")
    #locationofmyitem = my_items.index(item)

# Dictionary-> key value paires  Tuples-immutable lists  Sets-> 


#HW-1
# Ask a person 3 times, if he wants to have spaghetti or not?
# add all of the answers of that person in that list
# then count the number of yes from that list
# and show him how many times he agreed to have spaghetti

prsn_ans=[]
first_ans=input("Do you want to eat spaghetti? Enter yes or no? ")
prsn_ans.append(first_ans)
scnd_ans=input("Do you want to eat spaghetti? Enter yes or no? ")
prsn_ans.append(scnd_ans)
thrd_ans=input("Do you want to eat spaghetti? Enter yes or no? ")
prsn_ans.append(thrd_ans)

print("------------------------")
print(prsn_ans)
print("-------------- ----------")
print(f"You entered yes {prsn_ans.count("yes")} times")

#tips
# grocery_task = tasks.index("do grocery")
# #STEP 2: Add 1 to the index
# book_task = grocery_task + 1
# #STEP 3: Insert the 'read book' task
# tasks.insert(book_task, "read book")

#tasks.insert(3, "do grocery")