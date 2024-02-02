# no need to declare data type
""" x = "a"
print(type(x))
"""
# add two string words

# var1 = "hello"
# var2 = "from"
# myName="Satish"


# print(var1+var2, myName, end="-") #<- if we want to end any line with special char instead of new line , use end

# print(var1,var2)

# print(f"hello from {myName}")

# get data from user
# input conside everything as string

# name = input("Please le me know your name? \n") #<- add space or \n ...if you add space it will be included in input, trim str before using
# print(f"you entered {name}!")

# print(type(name))

#age = input("Please le me know your age in numeric? \n") 

#age = int(input("Please le me know your age in numeric? \n")) #<- elimate error by converting right at input function

age = input("Please le me know your age in numeric? \n")

#print(isinstance(age,int))
print("is instance of int ", isinstance(age,int))

#print(age.isnumeric())
print("is instance of float ", isinstance(age,float))

#age=int(age)
age=float(age)

print("after conversion , is instance of float ", isinstance(age,float))

print(f"you entered {age}!")
#age=age+10 #<- not allowed, only concatinate str with str...
age+=10 # there is no ++ , use +1 for increment , same for --

print(f"after 10 years your age will be {age}!")

grocery = ["apples", "bananas", "pineapples"]
print(grocery)



