# Normal, Deep and Shallow Copy.
import copy

print("\nIn python, new objects have the same ID as the old one.",
"Hence, changes made to one object will affect all its other copies.\nExample :\n")
print()
print("Normal Copy : ")
a = [1,2,3,4,5]
print("List A :",a)
a_temp = a
print("Temp List :",a_temp)
a_temp[0]=0
print("After updating Temp List :",a_temp)
print("Status of List A after updating Temp List :",a)
print("This is because, ID of both the lists are the same.")
print("ID of List A :",id(a))
print("ID of Temp List :",id(a_temp))

print("\nShallow copy :")
a = [1,2,3,4,5]
a_temp = copy.copy(a)           # Have to import copy.
print("List A :",a)
print("Temp List :",a)
a_temp[0]=0
print("After updating Temp List :",a_temp)
print("Status of List A after updating Temp List :",a)
print("ID of List A :",id(a))
print("ID of Temp List :",id(a_temp))

print("\nDeep copy :")
print("In Deep Copy, the old object and the new object and entirely Independant of each other.")
a = [1,2,3,4,5]
a_temp = copy.deepcopy(a)           # Have to import copy.
print("List A :",a)
print("Temp List :",a)
a_temp[0]=0
print("After updating Temp List :",a_temp)
print("Status of List A after updating Temp List :",a)
print("ID of List A :",id(a))
print("ID of Temp List :",id(a_temp))
