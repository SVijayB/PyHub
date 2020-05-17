# You can also copy data between two files using File Handling.

path1 = "assets\Random.txt"
path2 = "assets\Message.txt"

x = open(path1 , "r")
data = x.read()             # Copying all the data using the read function.
x.close()

y = open(path2 , "a")       # Opening it in append mode to avoid losing previous data.
y.write("\n"+data)          # Writing the copied data into the second file.
y.close()
input("Press any key to exit ")