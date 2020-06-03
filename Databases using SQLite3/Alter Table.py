import sqlite3

db = sqlite3.connect("assets/Student_records.db")
cursor = db.cursor()

query = """ALTER TABLE Students RENAME TO Student_records ADD COLUMN E-mail """
cursor.execute(query)
db.commit()
db.close()
input("Press any key to exit ")