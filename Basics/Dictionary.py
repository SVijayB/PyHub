print("Dictionary in Python is an unordered collection of data values, "+
"used to store data values like a map, which unlike other Data Types that hold "+
"only single value as an element, Dictionary holds key:value pair. Key value is provided in "
"the dictionary to make it more optimized.")
print()
print("For dictionaries in python, we use curly brackets")
a = {1 : 'Hey', 2 : 'How', 3 : 'What'} 
print("A : " , a)
b= dict({1 : 'Hello', 2 : 'World', 3 : '!'}) 	#Dictionary Function
print("B : " , b)
print("First element in A :",a[1])	
a[4] = 'Awesome'								#Adding value to the dictionary
print("After adding element to A : " , a)
b[2] = 'There'									#Updating
print("After updating element in B : " , b)
del a[3]										#Deleting
print("After deleting the 3rd element in A : " , a)
a.clear() 										#Deleting entire Dictionary
print("After deleting entire dictionary A : " , a)
dict = {"a":1, "b":2, "c":3, "d":4}
z = dict.items()
print(z)
x = dict.keys()
print(x)
y = dict.values()
print(y)
temp1 = "hello"
temp2 = "wow"
dict.update({temp1:temp2})
print(dict)
input("Press Enter key to exit ")