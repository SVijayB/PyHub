# Order By Clause is used to order the record in an ascending or descending order.
import sqlite3

Connection = sqlite3.connect("Databases using SQLite3/assets/Student_Records.db")
print("Connection has been made successfuly!")
cursor = Connection.cursor()
query = """SELECT NAMES,MARKS FROM Student_Records ORDER BY NAMES ASC"""    # Use DESC for descending
cursor.execute(query)
records = cursor.fetchall()
for x,y in records:
    print(x,y)

print("\nArranging my marks obtained")
query = """SELECT NAMES,MARKS FROM Student_Records ORDER BY MARKS DESC"""    
cursor.execute(query)
records = cursor.fetchall()
for x,y in records:
    print(x,y)
Connection.close()