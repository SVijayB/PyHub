import sqlite3

connection = sqlite3.connect("assets/Student_records.db")
print("Connection has been made successfuly!")
cursor = connection.cursor()  # Control structure for traversal over record in DB.
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (1, "Vijay", 78, "B"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (2, "Balaji", 65, "C"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (3, "Stark", 100, "A"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (4, "Steve", 42, "D"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (5, "Barney", 64, "C"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (6, "Sid", 73, "B"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (7, "Bucky", 53, "C"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (8, "Raj", 94, "A"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (9, "Adi", 87, "A"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (10, "Barton", 57, "C"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (11, "Naruto", 34, "F"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (12, "Sasuke", 68, "C"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (13, "Madara", 47, "C"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (14, "Will", 38, "D"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (15, "Dave", 27, "F"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (16, "Dan", 87, "A"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (17, "Amy", 98, "A"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (18, "Ron", 14, "F"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (19, "Percy", 34, "F"),
)
cursor.execute(
    """INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",
    (20, "Leo", 78, "B"),
)
print("Records have been added")
connection.commit()
connection.close()
input("Press Enter key to exit ")
