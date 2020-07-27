"""
Program defination : 
For two positive integers, lo and hi, and a limit k, find two integers,a and b, satisfying the following criteria.
Return the value of a*b. The * symbol denotes the bitwise xor operator. Write a python function to return the value
of a*b. The function will accept lo, hi, and k values as input arguments.
lo <= a < b <= hi, the value of a*b is minimal for a*b <= k.

Example : lo = 3, hi = 5, k = 6.
                                                ╔═════╦═════╦═════╗
                                                ║ a   ║ b   ║ a*b ║
                                                ╠═════╬═════╬═════╣
                                                ║ 3   ║ 4   ║ 7   ║
                                                ╠═════╬═════╬═════╣
                                                ║ 3   ║ 5   ║ 6   ║
                                                ╠═════╬═════╬═════╣
                                                ║ 4   ║ 5   ║ 1   ║
                                                ╚═════╩═════╩═════╝

The maximal usable XORed value is 6 because it is the maximal value that is less thank or equal to the limit k = 6.
"""
def calculator(lo, hi, k):
    a = lo
    b = a + 1
    max = -1
    while(a<b and b<=hi):
        while(b<=hi):
            value = (a^b)
            print(a, "xor", b, "=", value)
            if(value > max and value <= k):
                max = value
            b = b + 1
        a = a + 1
        b = a + 1
    print("Maximal value is", max)
    
if __name__ == "__main__":
    lo = int(input("Enter one number : "))
    hi = int(input("Enter the second number : "))
    k = int(input("Enter the limit : "))
    print("Results : ")
    calculator(lo, hi, k)