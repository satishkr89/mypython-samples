# for i in range(1,5): #last number is not inclusive
#     print(f"counter is {i}")
    
# for i in range(5): # use tis techniq when dealing with lists
#     print(f"counter is {i} when only range is defined")
    
    
# for i in range(1,5,2): # a
#     print(f"counter is {i} when range starts with 1 and takes two steps/jump")


# records=5
# counter=1    
# while (counter <= records):
#     print(f"counter is {counter} records numer is {records}")
#     records-=1

while(True):
    cc_num = input("Please enter your credit card number: ")
    if(len(cc_num)==16):
        print("you are hacked")
        break
    
    
