# A generator is a function that has a yield statement instead of a return statement.
# It is used to create iterables.
print("Without Using Yield Statemenet")
def x():
    return "a"
    return "b"
    return "c"

y = x()
for i in range(3):
    print(y)

print("\nUsing the Yield Statemenet")
def x():
    yield "a"
    yield "b"
    yield "c"

y = x()
for i in range(3):
    print(y.__next__())

"""
print("\nExample 2 : ")
print("Without Using Yield Statemenet")
def calls_recieved(recieved):
    a = 0
    while(True):
        if(recieved=="yes"):
            a = a+1
            return a
        else:
            return a

while (True):
    recieved = input("Did you recieve a call or not? : ")
    total = calls_recieved(recieved)
    print(total)   
"""

print("\nUsing the Yield Statemenet")
def calls_recieved(recieved=None):
    a = 0
    while (True):
        if recieved == "yes":
            a = a+1
            recieved = yield a
        else:
            recieved = yield a

rec = calls_recieved()
rec.__next__()
       
while (True):
    ans = input("Did you recieve a call or not? : ")
    print(str(rec.send(ans)))  

input("Press Enter key to exit ")