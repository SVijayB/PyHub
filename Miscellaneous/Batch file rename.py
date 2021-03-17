import os

"""
Program Description : 
Batch file rename is a program created to solve renaming problems. Especially when it comes down to
downloading a large number of image files and then renaming them one by one. With this, you can rename 
all of them within seconds.

Note : The program renames only image files(.jpg) at the moment. Other extensions and file types will be 
worked upon later.
"""


def rename():
    i = 0
    path = input("Enter the path of the folder in which files are present \n> ")
    name = input("Enter the name to which you want to rename all the files into \n> ")
    for filename in os.listdir(path):
        dest = name + str(i) + ".jpg"
        initial = path + "\\" + filename
        final = path + "\\" + dest
        os.rename(initial, final)
        i = i + 1

    print("Files have been renamed succesfully!!")


if __name__ == "__main__":
    rename()
    input("Press Enter key to exit ")
