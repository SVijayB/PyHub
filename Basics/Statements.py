# Break Statement : 

greetings = ["Hello","World","!!!"]
for x in greetings:
    print(x)
    if (x == "World"):
        break           #Breaks the loop when condition matches

print()

for x in range (0,22,2):
    if (x == 10):
        continue        #Skips the current iteration when condition matches 
    print(x)
input("Press Enter key to exit ")
