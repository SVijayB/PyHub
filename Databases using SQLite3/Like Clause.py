import sqlite3

connection = sqlite3.connect("assets/Student_records.db")
cursor = connection.cursor()
print("PRINTING NAMES STARTING WITH A")
query = """SELECT NAMES,MARKS FROM Student_Records WHERE NAMES LIKE 'a%' """    # Names starting with a
cursor.execute(query)
student_record = cursor.fetchall()
for names,marks in student_record:
    print(names,marks)
connection.close()

print("\nPRINTING NAMES ENDING WITH I")
connection = sqlite3.connect("assets/Student_records.db")
cursor = connection.cursor()
query = """SELECT NAMES,MARKS FROM Student_Records WHERE NAMES LIKE '%i' """    # Names ending with a
cursor.execute(query)
student_record = cursor.fetchall()
for names,marks in student_record:
    print(names,marks)
connection.close()

print("\nPRINTING NAMES WITH ID IN THEM")
connection = sqlite3.connect("assets/Student_records.db")
cursor = connection.cursor()
query = """SELECT NAMES,MARKS FROM Student_Records WHERE NAMES LIKE '%id%' """    # Names that has id in them
cursor.execute(query)
student_record = cursor.fetchall()
for names,marks in student_record:
    print(names,marks)
connection.close()
input("Press any key to exit ")