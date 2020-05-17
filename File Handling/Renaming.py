# Renaming a file using the OS module.
import os

try:
    os.rename("assets\Random.txt","assets\Message.txt")
except FileNotFoundError:
    print("\nERROR : File does not exist! Check your path or the file name once again")
def doc():
    """
The rename function takes two arguments, the first is the path to the file you want to change the name.
Second is the name of the file you want to change it to(Make sure you add path as well).
    """
print(doc.__doc__)
input("Press any key to exit ")