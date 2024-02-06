#Conditional Operations

# <, >, ==, <=, >=, !=, True, False , +=, -+, 

# no switches in py


# fruit = "apple"

# if fruit=="cherry":
#     print("We got cherries")
# elif fruit=="apple":
#     print("We got apple")
# else:
#     print("we didn't get cherries")


# fruit = ["apple", "chery"]

# if "chery" in fruit :
#     print("We got cherries")
# elif "apple" in fruit:
#     print("We got apple")
# else:
#     print("we didn't get cherries")
    
# assign grades based on student marks



# name = input("Please enter student name ")

# marks = float(input("Please enter student marks "))

# print(f"you entered student {name} and his/her marks {marks}")
# if marks >= 90:
#     print(f"Student {name} got grade A")
# elif marks >= 80:
#     print(f"Student {name} got grade B")
# elif marks >= 70:
#     print(f"Student {name} got grade C")

# if marks <= 70:
#     print(f"Student {name} got grade C")
# elif (marks >= 70  <= 80): # do not use & it is a bitwise operator 
#     print(f"Student {name} got grade B")
# elif marks >= 90:
#     print(f"Student {name} got grade A")

#hw - calculator


# ask for any two numbers from the user
#  Enter first number:
#  Enter second number: 
# ask the user if he wants to select addition, multiplication or division
#  Select option:
    #  Press 'a' for Addition
    #  Press 'm' for Multiplication
    #  Press 'd' for Division
    # if the user selects addition - add the two numbers and show the answer
    # if the user selects multiplication - multiply the two numbers and show the answer
    # if the user selects division - divide the two numbers and show the answer
    
# print("this is satish's calculator")
# firstnum = int(input("enter first number : "))
# scndnum = int(input("enter second number: "))
# print("Press 'a' for Addition")
# print("Press 'm' for Multiplication")
# print("Press 'd' for Division")

# ops = input("enter arithmatic operation you want? ")

# if ops == 'a':
#     print(f"{firstnum} added to {scndnum} is equal to {firstnum+scndnum}")
# elif ops == 'm':
#     print(f"{firstnum} Multiplication to {scndnum} is equal to {firstnum*scndnum}")
# elif ops == 'd':
#     print(f"{firstnum} Division to {scndnum} is equal to {firstnum/scndnum}")
# print("done")
# try:
#     print("this is satish's calculator")
#     while(True):
        
#         firstnum = int(input("enter first number : "))
#         scndnum = int(input("enter second number: "))
#         print("Press 'a' for Addition")
#         print("Press 'm' for Multiplication")
#         print("Press 'd' for Division")
#         print("Press 'q' to quit calculator")

#         ops = input("enter arithmatic operation you want? ")

#         if ops == 'a':
#             print(f"{firstnum} added to {scndnum} is equal to {firstnum+scndnum}")
#         elif ops == 'm':
#             print(f"{firstnum} Multiplication to {scndnum} is equal to {firstnum*scndnum}")
#         elif ops == 'd':
#             print(f"{firstnum} Division to {scndnum} is equal to {firstnum/scndnum}")
#         elif ops == "q":
#             print("quitting calculator")
#             break
# except:
#     print("Exception....")


# make an area calculator:
    # ask the user for which shape he wants to calculate the area:
    #  Select option:
    #  Press 't' for triangle
    #  Press 's' for square
    #  Press 'r' for rectangle
    #  Press 'c' for circle
    # if it's a triangle
    # ask the user to enter base and height of triangle
    # use the formula 1/2 * Base * Height to find the area of the triangle
    # if it's a square
    # ask the user to enter the length of one side of square
    # use the formula length * length to find the area of the square
    # if it's a rectangle
    # ask the user to enter the length and width of rectangle
    # use the formula length * width to find the area of the rectangle
    # if it's a circle
    # ask the user to enter the radius of the circle
    #use the formula 3.14 * radius ** 2 to find the area of the circle

try:
    print("Welcome to area calculator")
    while(True):
        print("Please selct shape you want to calculate the area for:")
        print("Press 't' for triangle")
        print("Press 's' for square")
        print("Press 'r' for rectangle")
        print("Press 'c' for circle")
        print("Press 'q' to quit area calculator")
        shapeType = input("enter shape type : ")

        if shapeType == 't':
            base = int(input("Enter base of triangle: "))
            height = int(input("Enter height of triangle: "))
            print("Calculating area for triangle")
            area_of_trngl = 1/2 * base * height 
            print(f"Area for triangle with base {base} and height {height} is {area_of_trngl}")
        
        elif shapeType == 's':
            sq_side_ln = int(input("Enter the length of one side of square: "))
            print("Calculating area for square")
            #area_of_sq = sq_side_ln * sq_side_ln 
            area_of_sq = sq_side_ln ** 2 
            print(f"Area for square with side {sq_side_ln} is {area_of_sq}")
        
        elif shapeType == 'r':
            rect_side1 = int(input("Enter one side of rectangle: "))
            rect_side2 = int(input("Enter another side of rectangle: "))
            print("Calculating area for rectangle")
            area_of_rectngl = rect_side1 * rect_side2 
            print(f"Area for rectangle with one side {rect_side1} and second side {rect_side2} is {area_of_rectngl}")
        
        elif shapeType == "c":
            crl_radious = float(input("Enter the radius of circle: "))
            print("Calculating area for circle")
            area_of_crl = 3.14 * (crl_radious ** 2)
            print(f"Area for circle with radious {crl_radious} is {area_of_crl}")
            
        elif shapeType == "q":
            print("quitting calculator")
            break
        
        else:
            print("Only supported shapes options are: t, s, r, c!")
except:
    print("Exception....")

