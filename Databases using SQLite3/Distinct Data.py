import sqlite3

db = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
print("Connection has been made successfuly!")
cursor = db.cursor()
query = """SELECT DISTINCT GRADES FROM Student_Records"""
cursor.execute(query)
records = cursor.fetchall()

for x in records:
    print(x)
db.commit()
db.close()