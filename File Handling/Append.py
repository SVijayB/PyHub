# Append mode is used to attach new data to the exisiting text file rather than overwriting it.
# Write Mode : 
path = "assets/File Handling/Random.txt"
file = open(path, "w")
file.write("Hey! This is the second message and it repalced the previous one!")
file.close()    
# Everytime you run the program, the lines are removed and the new ones are added.
# Append mode : 
file = open(path, "a")
file.write("\nNow, data won't be lost! That's because the file is opened in append mode.")
file.close()