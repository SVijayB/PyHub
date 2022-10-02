#check if the number is palindrome
def check_pali():
    n = input("Enter the number: ")
    if n[::] == n[::-1]:
        print("THE NUMBER IS A PALINDROME")
    else:
        print("THE NUMBER IS NOT A PALINDROME")
    return

#printing palindrome numbers in a range
def print_pali():
    a = list(map(int,input("Enter the range of numbers: ").split(" ")))
    res = []
    for i in range(a[0],a[1]):
        i = str(i)
        if i == i[::-1]:
            res.append(i)
    print("\nTHE PALINDROME NUMBERS ARE: ")
    for j in res:
        print(j)
    return 

if __name__ == "__main__":
    while(1):
        m = int(input("\n1.Check if number is palindrome\n2.Print all palindrome numbers in a range\n3.Exit\n"))
        if m == 1:
            check_pali()
        elif m == 2:
            print_pali()
        elif m == 3:
            exit(1)
    