import sqlite3

print("LIMITING RECORD TO FIRST 3")
db = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
print("Connection has been made successfuly!")
cursor = db.cursor()
query = """SELECT ID,NAMES FROM Student_Records LIMIT 3"""
cursor.execute(query)
records = cursor.fetchall()
for x,y in records:
    print(x,y)
db.commit()
db.close()

print("\nLIMITING RECORDS FROM 4-7")
db = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
print("Connection has been made successfuly!")
cursor = db.cursor()
query = """SELECT ID,NAMES FROM Student_Records LIMIT 3 OFFSET 4""" # Use Offet to set starting pos.
cursor.execute(query)
records = cursor.fetchall()
for x,y in records:
    print(x,y)
db.commit()
db.close()