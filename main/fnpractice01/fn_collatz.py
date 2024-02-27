# The Collatz Sequence

# Task1: Write a function named collatz() that has one parameter named number. 

# Task2: Inside the function, if number is even, then collatz() should print number // 2 and return this value

# Task3: If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
   if number % 2 == 0:
      print(f"The number: {number} // 2 ")
      return number % 2
   else:
      print(f"The number: 3 * {number} + 1")
      return 3 * number + 1

try:
   print("This is even / odd number teller.")
   while(True):
      num1 = input("enter a number between or q for quitting : ")
      if num1 == "q":
         print("quitting even / odd teller")
         break
      else:
         collatz(int(num1))
except Exception as exp:
        print("Exception....->", type(exp), exp )