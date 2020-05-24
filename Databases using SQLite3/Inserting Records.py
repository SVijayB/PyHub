import sqlite3

connection = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
print("Connection has been made successfuly!")
cursor = connection.cursor()    # Control structure for traversal over record in DB.
cursor.execute("""INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",(1,"VIJAY",85,"A"))
cursor.execute("""INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",(2,"BALAJI",65,"B"))
cursor.execute("""INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",(3,"STARK",100,"A"))
cursor.execute("""INSERT INTO Student_Records(ID,NAMES,MARKS,GRADES)VALUES(?,?,?,?)""",(4,"STEVE",40,"C"))
print("Records have been added")
connection.commit()
connection.close()