x = set([1,2,3])
print("Set X : " , x)
y = set([3,4,5])	
print("Set Y : " , y)
union = x.union(y) 
print("X union Y : " , union)
intersection  = x.intersection(y)
print("X intersection Y : " , intersection)
diff = x - y  		#elements present in x that are not present in y
print("X - Y : " , diff)
sysdiff = x^y 		#Symetric difference -> uncommon elements in both x and y
print("Uncommon elements in both X and Y : " , sysdiff)
z = x.issubset(y) 	#checks if x is a subset of y or not. Returns true or false.
print("Is X a subset of Y ?" , z)

#You can also add or remove an element from the set by using add and remove function, eg : 
x.add(5) 			# adds 5 to set x
print("After adding 5 to set X : " , x)
y.remove(5) 		#removes 5 from set y
print("After removing 5 from set Y : " , y)