def isHappy(n): 
    numbers = []
    numbers.append(n) 
    while (True): 
        sum = 0; 
        while (n!=0): 
            digit = n % 10
            sum = sum + (digit * digit)
            n = n // 10
        n = sum
        if n in numbers: 
            return False
        elif (n == 1): 
            return True
        else:
            numbers.append(n) 

if __name__ == "__main__":
    n = int(input("Enter the number to check \n> "))
    if (isHappy(n)): 
        print("Yes")  
    else: 
        print("No") 