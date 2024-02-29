class Pirate:
    pirate_list = []
    def __init__(self, name, password, work, number_of_eyes):      #password and name of the pirate,
                                                                 #the work he does on the pirate ship,
                                                                 #number of eyes he has - because most pirates have only one eye... Errrrrrr!!!!
        self.name = name
        self.work = work
        self.eyes = number_of_eyes
        self.password = password
        self.pirate_list = []
        #new_pirate = Pirate(self.name, self.password, self.work, self.eyes)
        #self.pirate_list.append(new_pirate)
    def display_all_pirates(self):
        for dakoo in self.pirate_list:
            print("---------Pirate List---------------")
            print(f"Name: {dakoo.get_name()}")
            print(f"Name: {dakoo.get_password()}")
            print(f"Work: {dakoo.work}")
            print(f"Eyes: {dakoo.eyes}\n")
            
    def get_name(self):                                          #return the name of the pirate (we will use this for login page)
        return self.name

    def get_password(self):                                      #return the password of the pirate (we will use this for login page)
        return self.password


    #---------HANDY DANDY FUNCTIONS---------
    #you always have to define the functions first

    def sign_up(self):
        print("------------------------")
        print("PIRATE REGISTRATION PAGE")
        print("------------------------")

        #---STEP 1: Ask for pirate details---
        name = input("Ahoy! What's your name?")
        work = input("Ye! What's your job on the Secret Pirate Ship?")
        number_of_eyes = int(input("Do you have only one eye or two? Errrrr!!! Give me a number mate!"))
        password = input("Hurry! Give me a password!")

        #---STEP 2 and 3: Create a pirate object and save the pirate details---
        new_pirate = Pirate(name, password, work, number_of_eyes)

        #---STEP 4: add the pirate to pirate list
        self.pirate_list.append(new_pirate)

        print("\n---Yo Ho! You have been added to the Secret Ship Pirate System---")

    #---------------------------------

    #update the log_in function

    def log_in(self):
        print("------------------------")
        print("PIRATE LOG IN PAGE")
        print("------------------------")

        #---STEP 1: Ask for pirate name and password---
        entered_name = input("Ahoy! What's your name?")
        entered_password = input("Tell your a password mate!")

        #---STEP 2: Check the name and passoword in the pirate list---
        for pirate in self.pirate_list:    #get every pirate in the pirate list
                                            #get the name of the pirate and match it with the entered_name
        #---STEP 3: If the name and password matches, Welcome the pirate to the ship---
            pirate_name = pirate.get_name()
            if(pirate_name == entered_name):                          #if the name matches successfully
                pirate_password = pirate.get_password()
                if(pirate_password == entered_password):                      #check if the password is correct
                    print("---Welcome to the Secret Pirate Ship mate!---")      #say welcome to the pirate
                    return                                                      #end this function right now and go back to the menu page (from where this log_in function was called)
#---STEP 4: If the name and password do not match, don't let him enter the ship---
                else:                                                         #if the password is wrong
                    print("---Sorry mate you have entered wrong password---")   #don't let him enter the ship
                    return                                                      #end this function right now and go back to the menu page (from where this log_in function was called)

        #you will only come outside the for loop if the pirate name was not matched in the whole pirate list
            print("---Errrr!!! You are a decoy, you can't use this ship!---")
        #---------------------------------


 


