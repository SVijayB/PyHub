import sqlite3

connection = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
cursor = connection.cursor()
print("Printing all records")
query = """SELECT NAMES,MARKS FROM Student_Records"""   # Select * For all attributes
cursor.execute(query)

student_record = cursor.fetchall()

for names,marks in student_record:
    print(names,marks)
connection.close()

print("\nPrinting a single record using fetchone")
connection = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
cursor = connection.cursor()

query = """SELECT NAMES,MARKS FROM Student_Records""" 
cursor.execute(query)

student_record = cursor.fetchone()

print(student_record)