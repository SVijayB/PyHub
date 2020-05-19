import sqlite3

try:
    database = sqlite3.connect("assets/Student_Records.db")  
    print("Connection has been made successfuly!")
    database.close()
except:
    print("Connection ERROR")
input("Click on any key to close ")