import sqlite3

try:
    database = sqlite3.connect("assets/Student_records.db")  
    print("Connection has been made successfuly!")
    database.close()
except:
    print("Connection ERROR")
input("Press any key to close ")