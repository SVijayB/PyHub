# Reading from a file.
path = "assets/File Handling/Random.txt"
print("Reading file at assets/File Handling with the name Random.txt")
file = open(path,"r")
# file.write("wow!") will show error, since the file is opened in read only mode.