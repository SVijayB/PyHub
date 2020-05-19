def doc():
    """
In Dictionary comprehensions, a new dictionary is made based on the old dictionary. It is created
to modify or add new contents/items to the dictionary.
It is a fast and efficient method.
    """
print(doc.__doc__)
print("Example 1 : ")
dict = {"a":1, "b":2, "c":3, "d":4}

new_dict_values = {k:v*2 for (k,v) in dict.items()}     # Multiplying all values by 2
print(new_dict_values)

new_key_values = {k*2:v for (k,v) in dict.items()}     # Multiplying all keys by 2
print(new_key_values)

print("Example 2 : ")
print("Without using comprehensions : ")
dict={}
for i in range(10):
    if i%2 == 0:
        dict[i]=i**2
print(dict)

print("Using comprehensions : ")
dict = {}
new_dict = {i:i**2 for i in range(10) if i%2==0}
print(new_dict)

print("\nDictionary Comprehensions as lambda functions : ")

