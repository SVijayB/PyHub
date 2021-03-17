# Coroutines are almost like generators. The only difference is the way we use the yield statement.
# We use coroutines to create a sequence, where one block executes, closes and gives control to the next.
def searching(string):
    print("Searching String : {}".format(string))
    while True:
        name = yield  # Recieved from the send function.
        if string in name:
            print(string + " is present in " + name)
        else:
            print(string + " is not present in " + name)


key = input("Enter the term you want to search for in string : ")
x = searching(key)
x.__next__()

while True:
    s = input("Enter the Strings : ")
    x.send(s)  # .send() is a built-in function.

input("Press Enter key to exit ")
