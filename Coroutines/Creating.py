# Coroutines are almost like generators. The only difference is the way we use the yield statement.
def searching(string):
    print("Searching String : {}".format(string))
    while True:
        name = (yield)      # Recieved from the send function.
        if string in name:
            print(name)
    
x = searching("Hello")
x.__next__()
    
x.send("Hello")             # .send() is a built-in function.
x.send("Hello World")
x.send("World")