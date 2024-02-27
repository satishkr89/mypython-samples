# Save the birthdays of any 4 people in a dictionary 
# Use person's name as key and the birthday as its value.

ppl_bd = {"Washington": "1/1/1800","Bush" : "2/2/1820", "Lincoln" : "3/3/1830", "Obama": "4/4/1840" }

# Task1: use a while loop and ask the user to enter any name or type 'stop' to stop the loop
# try:
#     print("This is birthday teller.")
#     while(True):
#         bd_name = input("Enter a name to get their birthday or stop for quitting birthday teller: ")
#         if bd_name == "stop":
#             print("quitting birthday teller")
#             break
#         else:
#             print(f"The birthday for {bd_name} ! is: {ppl_bd[bd_name]}")
# except:
#     print("Exception....")
    

# Task2: inside the loop Check if the person's name is present in the dictionary
#        if the name is present then show the person's name along with his birthday

# try:
#     print("This is birthday teller.")
#     while(True):
#         bd_name = input("Enter a name to get their birthday or stop for quitting birthday teller: ")
#         if bd_name == "stop":
#             print("quitting birthday teller")
#             break
#         else:
#             if bd_name in ppl_bd.keys():
#                 print(f"The birthday for {bd_name} ! is : {ppl_bd[bd_name]}")
#             else:
#                 print(f"The birthday for {bd_name} ! is not recorded.")
# except:
#     print("Exception....")



# Task3: if the person's name is not present in the dictionary then
#        show a message that this person's birthday is not saved
#        ask for the birthday for the person who is not in the dictionary
#        save this new person along with his birthday in the dictionary
# Task4: when the loop stops show the final dictionary

try:
    print("This is birthday teller.")
    while(True):
        bd_name = input("Enter a name to get their birthday or stop for quitting birthday teller: ")
        if bd_name == "stop":
            print("quitting birthday teller")
            break
        else:
            if bd_name in ppl_bd.keys():
                print(f"The birthday for {bd_name} ! is : {ppl_bd[bd_name]}")
            else:
                print(f"The birthday for {bd_name} ! is not recorded.")
                new_name_bd = input(f"Enter {bd_name}'s birthday: ")
                ppl_bd[bd_name] = new_name_bd
    print("========================================")
    print(f"These are birthday teller's final records: {ppl_bd}")
    print("========================================")
except:
    print("Exception....")
