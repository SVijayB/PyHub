# Creating a new text file.
path = "assets/File Handling/Random.txt"        # Remember to enter the file name you want to create.
print("Creating a file at assets/File Handling with the name Random.txt")
file = open(path, "w+")    
def doc():
    """
Modes by which you can open files in python : 
Files are opened using the open function in python, that takes the name and mode as argument.
Different modes : 
1) r : Used to open a file for reading.
2) w : For writing. If file already exists, it will delete all the pre-existing data.
3) x : Used to open a file for exclusive creation. Failing if the file already exists.
4) a : Used for writing and apppending to the file if it already exists.
5) b : binary mode.
6) t : text mode.
7) +r : Open a file for updating. Reading or Updating.
8) w+ : Used to create a text file or any other types.
    """                     
print(doc.__doc__)