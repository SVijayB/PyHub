import sqlite3

connection = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
cursor = connection.cursor()
print("BEFORE UPDATING : ")
query2 = """SELECT * FROM Student_Records WHERE ID = 6"""
cursor.execute(query2)
records = cursor.fetchall()
for id,name,mark,grade in records:
    print(id,name,mark,grade)
print("\nAFTER UPDATING : ")
query = """UPDATE Student_Records SET MARKS = 73,GRADES='B' WHERE ID = 6"""    # Names starting with a
cursor.execute(query)
query2 = """SELECT * FROM Student_Records WHERE ID = 6"""
cursor.execute(query2)
records = cursor.fetchall()
for id,name,mark,grade in records:
    print(id,name,mark,grade)
connection.commit()
connection.close()