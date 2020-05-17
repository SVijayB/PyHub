print("Lists are a collection of elements. They are mutable. They can have Strings, numbers, Float and more " +
"or a combination of all of them")

print("For lists we use Sqare brackets.")
a = [1,2,"Hey!",4,"Wow"]
print("List A :" , a)
print()

print("Each element has an unique index. It starts with 0.")
print()

print("Third element in A :" , a[2])
a[2] = "Awesome!"
print("After updating 3rd element in A :", a[2])
a.insert(0,"Cool")
print("After adding a new element to A : " , a)
a.remove("Wow")
print("After removing the element \"Wow\":", a)
a.reverse()
print("After reversing the list :" , a)
input("Press any key to exit ")