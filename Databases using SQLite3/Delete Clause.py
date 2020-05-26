import sqlite3

print("DELETING RECORD WITH ID = 6")
db = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
query = """DELETE FROM Student_Records WHERE ID = 6"""
cursor = db.cursor()
cursor.execute(query)
db.commit()
query = """SELECT * FROM Student_Records"""   # Select * For all attributes
cursor.execute(query)
student_record = cursor.fetchall()
for id,names,marks,grades in student_record:
    print(id,names,marks,grades)

