
# Dictionary-> key value paires  Tuples-immutable lists  Sets-> 
# numpy works based on lists and pandas based on Dictionary


dict_vehicals = {"Make":"Ford", "Model":"eMac", "FuelType":"Electric"}
print("Initial inventory of vehicals: ", dict_vehicals)

dict_vehicals["price"] = 10000
print("inventory of vehicals with price: ", dict_vehicals)

dict_vehicals["price"] = 15000
print("inventory of vehicals with price updated: ", dict_vehicals)

dict_vehicals.pop("FuelType")
print("Inventory of vehicals: ", dict_vehicals)

print("length of vehical attributes: ", len(dict_vehicals))

print("keys of vehical attributes: ", dict_vehicals.keys())
print("values of vehical attributes: ", dict_vehicals.values())
print("items of vehical attributes: ", dict_vehicals.items()) #returns list of tuples 

for i in dict_vehicals:
    #print(f"keys in dictionary are {i}")
    print(f"key value in dictionary are {i} : {dict_vehicals[i]}")
print("----------------") 

for i in dict_vehicals.keys():
    print(f"key value in dictionary are {i} : {dict_vehicals[i]}")
    
print("----------------") 

for i in dict_vehicals.values():
    print(f"Value in dictionary are {i}")

print("----------------") 

for i in dict_vehicals.items():
    print(f"Value in dictionary are {i}")
    
    print("----------------") 

for k, v in dict_vehicals.items():
    print(f"Item in dictionary are Key is {k}:{v}")

