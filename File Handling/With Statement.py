def doc():
    """
    Using the with statement, you can get better syntax and exception handling.
    The with statement simplifies exception handling by encapsulating common preparation and cleans up tasks.
    File is automatically closed using the with statement.
    """


print(doc.__doc__)

path = "assets\Random.txt"

with open(path, "a") as file:
    file.write("\nThis message is appended using the with statement")
input("Press Enter key to exit ")
# file.write("With statement!") if you run this line, it would show errors as the with statement closes the file automatically.
