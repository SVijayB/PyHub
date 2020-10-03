import sqlite3

db = sqlite3.connect("assets/Student_records.db")
print("Connection has been made successfuly!")
cursor = db.cursor()
query = """SELECT DISTINCT GRADES FROM Student_Records"""
cursor.execute(query)
records = cursor.fetchall()

for x in records:
    print(x)
db.commit()
db.close()
input("Press Enter key to exit ")