class DCalculator:

# -------------------------------
# Dynamic Calculator

# Task1: Make a function called perform_operation() with 4 arguments of value1, value2, is_list, mode
# This function can accept both numbers and lists as value1 and value2. 
# The default value of is_list is False and the default value of mode is add.
# One can set is_list to either True or False.
# One can set mode to add, avg or max_avg. 
# Add can be set in the case of both numbers and lists 
# but avg is only used for numbers and max_avg is only used in case of lists
# Task2: If is_list is False: check if both value1 and value2 are numbers (int or float).
# If not show an error and return 'Argument Value Mismatch'

# Task3: If is_list is True: check if both value1 and value2 are lists.
# If not show an error and return 'Argument Value Mismatch'

# Task4: If mode is set something other than add or avg, show an error and return 'Specified Mode Does Not Exist'
#        If is_list is True and mode is avg, show an error and return 'Mode Mismatch'
#        If is_list is False and mode is max_avg, show an error and return 'Mode Mismatch'

# Task4: If mode is add and is_list is False: 
#               the add two numbers and return the answer

# Task5: If mode is add and is_list is True: 
#               the add corresponding indices of both lists and return the answer
#               For this you can even use built in functions for lists to add both lists

# Task6: If mode is avg and the is_list is False: 
#               take the average of two numbers and return the answer

# Task7: If mode is avg and is_list is True: 
#               Find the avg of both lists separately
#               Find the maximum of the two averages and return the answer
#               For this you can even use built in functions for lists to add both lists

    def __init__(self):
        pass
    
    def perform_operation(self, value1, value2, is_list=False, mode="add"):
            print(f"perform_operation funcation called with values:")
            print(f"perform_operation--value1--->{value1}")
            print(f"perform_operation--value1--->{value2}")
            print(f"perform_operation--value1--->{is_list}")
            print(f"perform_operation--value1--->{mode}")
            
            try:
                o_result=0
                if is_list != True:
                    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                        if mode == "add" or mode == "avg" :
                            print("values are numbers and mode is ok too")
                            if mode == "add":
                                o_result= value1+value2  
                            elif mode == "avg":
                                o_result= (value1+value2)/2
                            else:
                                print("Specified Mode Does Not Exist")
                        else:
                            print("Specified Mode Does Not Exist")
                    else:
                        print("Argument Value Mismatch")
                else:
                    if isinstance(value1, list) and isinstance(value2, list):
                        print("values are numbers and mode is ok too")
                        if mode == "add":
                            o_result=sum(value1)+sum(value2)
                            print(f"Adding numbers from list .... total is: {o_result} ")
                        elif mode == "max_avg":
                            if (sum(value1))/2 > sum(value2)/2:
                                o_result=sum(value1)/2
                            else:
                                o_result=sum(value2)/2
                        else:
                            print("Specified Mode Does Not Exist")  
                    else:
                        print("Either one or both values are not lists")  
                return o_result
            except:
                print("Exception....")