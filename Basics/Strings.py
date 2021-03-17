# Both single and double quotes work.
a = "hello"
b = "world!"
print(a + " " + b)
print()

x = "aWeS0Me"
print("String is " + x)
print("Capitalizing the first letter : " + x.capitalize())
print("Converting stirng to lower case : " + x.casefold())
print("Converting all the letters to upper case : ", x.upper())
print(
    'Number of times "e" shows up in the string :', x.count("e")
)  # You cannot concat numbers and string, hence use ","
print("Does string end with a ? ", x.endswith("a"))
print("Does string end with e ? ", x.endswith("e"))
print('Where is the first "e" located at ?', x.find("e") + 1)
print("Are all the letters alphabets ? ", x.isalpha())
print("Making it a 10 charactered string : ", x.zfill(10))
print()

x = "Hey there I am vijay!"
print("New String : " + x)
y = x.partition("vijay")
print("Seperating vijay from string : ", y)
y = x.replace("vijay", "1StranGe")
print("After replacing terms in string : " + y)
print("Capitalizing the first letter of each word : ", x.title())
input("Press Enter key to exit ")
