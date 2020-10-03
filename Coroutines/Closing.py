def searching(string):
    print("Searching String : {}".format(string))
    while True:
        name = (yield)      
        if string in name:
            print(string + " is present in " + name)
        else:
            print(string + " is not present in " + name)
    
key = input("Enter the term you want to search for in string : ")
x = searching(key)
x.__next__()

while(True):
    s = input("Enter the Strings(Type quit to exit) : ")
    if(s!="Quit" and s!="quit"):
        x.send(s)
    else:
        x.close()       # Once closed you cannot pass again. 
        print("Coroutine Closed")
        break

input("Press Enter key to exit ")