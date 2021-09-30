# Find the middle letter in String.

def middle():
    s = input("Enter a string: ")
    if(len(s) % 2 != 0):
        print("Middle letter is: ", s[int(len(s)/2)])
    else:
        print("Middle letters are:",  s[int(len(s)/2) - 1], s[int(len(s)/2)])

if __name__ == "__main__":
    middle()