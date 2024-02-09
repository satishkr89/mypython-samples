#Arithmatic Operations

# math liberary has more funtions

#floor Division

# a = 14
# b = 5

# c = a/b #division

# print(f" adivided by b is {c}")

# d = a//b #floor division

# print(f" a floor divided by b is {d}")

# e=a%b  #mod

# print(f" a mod by b is {e}")

# d= a**b  # 14 raise to power 5

# f = 2**32
#print(f"a raise to power b i {f}")

#name = input("Please enter student name ")

#marks = float(input("Please enter student marks "))

# print(f"you entered student {name} and his/her marks {marks}")
# if marks >= 90:
#     print(f"Student {name} got grade A")
# elif marks >= 80:
#     print(f"Student {name} got grade B")
# elif marks >= 70:
#     print(f"Student {name} got grade C")

# if  70 <= marks < 80:
#     print(f"Student {name} got grade C")
# elif (marks >= 80 and marks < 90):
#     print(f"Student {name} got grade B")
# elif marks >= 90:
#     print(f"Student {name} got grade A")
    
#hw 
# boolean operators -> and or not <- need operand on both side 

# To Do:
# Now you can try to make a number finder that asks for a number from the user and checks that:

# if the number is zero - it says something like "oops it's a zero"
# if the number is between 1 and 5; OR; the number is between -1 and -5,then it says something like it's a low number
# if the number is between 6 and 10; OR; the number is between -6 and -10,then it says something like it's a high number
# if the user enters any number other number then it says like it's just a regular number

try:
    print("The number finder")
    while(True):
        num_entered = input("Please enter a number :")
        if num_entered == "q":
            print("quitting number finder")
            break
        num_entered=int(num_entered)
        if(num_entered ==0):
            print(f"You entered {num_entered}, oops it's a zero")
        elif ((1<num_entered<5) or (-1 > num_entered > -5)) :
            print(f"You entered {num_entered}, it's a low number")
        elif((6<num_entered<10) or (-6 > num_entered > -10)) :
            print(f"You entered {num_entered}, it's a high number")
        else:
            print(f"You entered {num_entered}, it's just a regular number")
        
except:
    print("Exception....")