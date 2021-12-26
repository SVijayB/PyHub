# Commit and push all changes of all repositories in a directory.
import os
import sys

if __name__ == "__main__":
    dir = input("Enter directory: ")
    if not os.path.isdir(dir):
        print("Invalid directory.")
        sys.exit(0)
    for root in os.listdir(dir):
        for file in os.listdir(os.path.join(dir, root)):
            if file.endswith(".git"):
                os.chdir(os.path.join(dir, root))
                os.system("git add .")
                os.system(
                    'git commit -m "Updated contact info"'
                )  # Adding your git commit message here.
                os.system("git push")
                print("Repository " + root + " updated.")
                os.chdir("..")