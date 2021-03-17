# A Glob operator is like a like operator but it is case sensitive and does not have any escape operators.

import sqlite3

db = sqlite3.connect("assets/Student_records.db")
cursor = db.cursor()

query = """SELECT NAMES FROM Student_Records where NAMES GLOB 'A*' """
# If you used a*, you can notice that it returns nothing. This is because glob operator is case sensitive
query2 = """SELECT NAMES FROM Student_Records where NAMES GLOB '?d*' """
# The ? signifies that there has to be atleast on character before d and the * signifies that there can be
# any character after d
query3 = """SELECT NAMES FROM Student_Records where NAMES GLOB '[A-D]*' """
# Elements have to start from letters from a-d

cursor.execute(query)
names = cursor.fetchall()
for x in names:
    print(names)

print()

cursor.execute(query2)
names = cursor.fetchall()
for x in names:
    print(names)

print()

cursor.execute(query3)
names = cursor.fetchall()
print(names)
input("Press Enter key to exit ")
