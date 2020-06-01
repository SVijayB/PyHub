import sqlite3

db = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
cursor = db.cursor()

query = """ALTER TABLE Students RENAME TO Student_records ADD COLUMN E-mail """
cursor.execute(query)
db.commit()
db.close()