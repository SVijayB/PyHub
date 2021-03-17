print(
    "List comprehension is an elegant way to define and create lists based on existing lists.",
    "list comprehensions are usually more human readable than lambda functions.",
    "It is easier to understand what the programmer was trying to accomplish when list comprehensions are used",
)
# Syntax :
# [expression (variable) for variable in input_set [predicate][,...]]

print("Example 1 : ")
x = set(i for i in range(10) if i % 2 == 0)
print(x)

print("Example 2 : ")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = set(i for i in list1 if i % 2 == 0)
print(x)

print("Example 3 : ")
x = set(
    (a, b) for a in range(3) for b in range(4)
)  # Nested for loop. a is external and b is internal
print(x)
