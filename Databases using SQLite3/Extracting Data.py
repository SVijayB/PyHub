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

print("\nPrinting multiple records using fetchone")
connection = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
cursor = connection.cursor()
query = """SELECT NAMES,MARKS FROM Student_Records""" 
cursor.execute(query)
student_record = cursor.fetchone()
while True:
    student_record = cursor.fetchone()
    if (student_record==None):
        break
    print(student_record)
print("\nNotice that it prints from the 2nd record, this is because we already printed the first one a while ago.",
"thus, the cursor points to the very next record.")