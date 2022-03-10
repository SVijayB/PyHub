#!/usr/bin/env python
# coding: utf-8

# In[8]:


num_roman = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "XD",
    500: "D",
    900: "CM",
    1000: "M",
}
num = int(input("Enter a number: "))

print_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

for x in print_order:
    if num != 0:
        rem = num // x

        if rem != 0:
            for y in range(rem):
                print(num_roman[x], end="")

        num = num % x


# In[ ]:
