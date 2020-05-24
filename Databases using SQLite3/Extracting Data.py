import sqlite3

connection = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
cursor = connection.cursor()

query = """SELECT NAMES,MARKS FROM Student_Records"""   # Select * For all attributes
cursor.execute(query)

student_record = cursor.fetchall()

for names,marks in student_record:
    print(names,marks)