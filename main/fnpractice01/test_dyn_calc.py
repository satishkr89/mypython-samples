from fn_dynamic_calc import DCalculator

val1=10
val2=5
is_list=False
#mode="add"
mode="avg"

dcalc = DCalculator()

result1 = dcalc.perform_operation(val1, val2, is_list, mode)

print(f"Result of operation is : {result1}")

#val1=[1,2,3,4,5]
val1=[1,2,3,4,5]
val2=[6,7,8,9,10]
is_list=True
mode="max_avg"

dcalc = DCalculator()

result1 = dcalc.perform_operation(val1, val2, is_list, mode)

print(f"Result of operation is : {result1}")