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