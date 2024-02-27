import math
import random


# volume of sphere = 4/3 pi r 3

#radius_of_sphere = int(input("Please enter radius of sphere : "))
radius_of_sphere = 2
vol_of_sphere = 4/3*math.pi*radius_of_sphere**3

#round the answer to 2 or 3 decimal points
#vol_of_sphere=round(vol_of_sphere, 4)

#print(f"Volume of sphere with radius {radius_of_sphere} is {vol_of_sphere}")
print(f"Volume of sphere with radius {radius_of_sphere} is {vol_of_sphere:.2f}") # format and print only 2 digits after decimal point


groceries = ["tomato", "beans", "apple", "carrot"]

# print(f"randomly selecting grocery item: " , random.choice(groceries))

# print(f"randomly printing numbers between 0 and 1 : " , random.random())

# print(f"randomly printing numbers from given range : " , random.randrange(100, 400))

# print(f"randomly printing int numbers : " , random.randint(1, 9999999)) #optionally providing range

random.shuffle(groceries) # it will change list

print(f"shuffeling groceries : " , groceries) 