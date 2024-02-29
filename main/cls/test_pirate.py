from Pirate import *

#Let's try to run the menu and see how it works
   #then you use the functions
    #---------PIRATE MENU PAGE---------
daakoo = Pirate("mangal", "kitneAadmiThe", "ducati", 2)
daakoo.pirate_list.append(daakoo)
while(True):
    #daakoo.display_all_pirates()
    print("\n\n------------------------")
    print("PIRATE MANAGEMENT SYSTEM")
    print("------------------------")
    print("Press 1. Sign Up")
    print("Press 2. Log In")
    print("Press 3. Exit")
    print("------------------------\n")
    choice = int(input("Your choice: "))

    if(choice == 1):
        daakoo.sign_up()                   #these functions are above

    if(choice == 2):
        daakoo.log_in()                        #these functions are above

    if(choice == 3):
        print("Thank you for using the Pirate Management System. Bye!!!")
        break

    #Let's try to run the menu and see how it works