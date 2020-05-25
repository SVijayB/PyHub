import sqlite3

db = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
print("Connection has been made successfuly!")
print("\nIN CLAUSE")
cursor = db.cursor()
query = """SELECT ID,NAMES,MARKS FROM Student_Records WHERE ID IN(2,4) ORDER BY NAMES ASC"""
cursor.execute(query)
records = cursor.fetchall()

for x,y,z in records:
    print(x,y,z)
db.commit()
db.close()

db = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
cursor = db.cursor()
print("\nNOT IN CLAUSE")
query = """SELECT ID,NAMES,MARKS FROM Student_Records WHERE ID NOT IN(2,4) ORDER BY NAMES ASC"""
cursor.execute(query)
records = cursor.fetchall()
for x,y,z in records:
    print(x,y,z)
db.commit()
db.close()