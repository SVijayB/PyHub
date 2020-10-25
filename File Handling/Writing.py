# Writing to a file.
path = "assets/Message.txt"

file = open(path,"w")
file.write("Hey! This is 1StranGe!")
file.write(" I am working on file handling in python.")

print("\nNote : Data is automatically saved in the file when the program is run.")
input("Press Enter key to exit ")