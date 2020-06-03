import sqlite3

print("DELETING RECORD WITH ID = 6")
db = sqlite3.connect("assets/Student_records.db")
query = """DELETE FROM Student_Records WHERE ID = 6"""
cursor = db.cursor()
cursor.execute(query)
db.commit()
query = """SELECT * FROM Student_Records"""   
cursor.execute(query)
student_record = cursor.fetchall()
for id,names,marks,grades in student_record:
    print(id,names,marks,grades)

print("\nDELETING RECORDS WHERE THE NAMES START WITH S")
db = sqlite3.connect("assets/Student_records.db")
query = """DELETE FROM Student_Records WHERE NAMES LIKE 's%'"""
cursor.execute(query)
db.commit()
query = """SELECT * FROM Student_Records ORDER BY NAMES ASC"""  
cursor.execute(query)
student_record = cursor.fetchall()
for id,names,marks,grades in student_record:
    print(id,names,marks,grades)

print("\nDELETING ALL THE RECORDS IN THE TABLE")
db = sqlite3.connect("assets/Student_records.db")
query = """DELETE  FROM Student_Records  """
cursor.execute(query)
db.commit()
query = """SELECT * FROM Student_Records"""   
cursor.execute(query)
student_record = cursor.fetchall()
for id,names,marks,grades in student_record:
    print(id,names,marks,grades)
db.close()
input("Press any key to exit ")