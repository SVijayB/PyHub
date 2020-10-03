import sqlite3
# In RDBMS, Attributes are columns of the table.
database = sqlite3.connect("assets/Student_records.db")
print("Connection has been made successfuly!")
database.execute("""CREATE TABLE Student_Records(ID INT PRIMARY KEY NOT NULL, 
NAMES TEXT NOT NULL, MARKS TEXT NOT NULL, GRADES NOT NULL)""")
print("Columns created in your Database")
database.close()
input("Press Enter key to exit ")
