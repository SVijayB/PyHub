def doc():
    """
In Dictionary comprehensions, a new dictionary is made based on the old dictionary. It is created
to modify or add new contents/items to the dictionary.
It is a fast and efficient method.
    """
print(doc.__doc__)
print("Example 1 : ")
dict1 = {"a":1, "b":2, "c":3, "d":4}

new_dict_values = {k:v*2 for (k,v) in dict1.items()}     # Multiplying all values by 2
print(new_dict_values)

new_key_values = {k*2:v for (k,v) in dict1.items()}     # Multiplying all keys by 2
print(new_key_values)

print("\nExample 2 : ")
print("Without using comprehensions : ")
dict2={}
for i in range(10):
    if i%2 == 0:
        dict2[i]=i**2
print(dict2)

print("Using comprehensions : ")
new_dict = {i:i**2 for i in range(10) if i%2==0}
print(new_dict)

print("\nDictionary Comprehensions as lambda functions : ")
farenheit = {1:10, 2:20, 3:30, 4:40}
cel_dict = {k:(float(5)/9)*(v-32) for (k,v) in farenheit.items()}
print(cel_dict)