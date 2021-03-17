import sqlite3


def fun(query):
    cursor.execute(query)
    foo = cursor.fetchall()
    for x in foo:
        print(x)
    print()


db = sqlite3.connect("assets/Student_records.db")
cursor = db.cursor()

query = """SELECT AVG(MARKS) FROM Student_records"""
fun(query)
query2 = """SELECT AVG(MARKS) FROM Student_records WHERE ID<7"""  # Average of first 6 students
fun(query2)
query3 = """SELECT MAX(MARKS) FROM Student_records"""
fun(query3)
query4 = """SELECT COUNT(*) FROM STUDENT_records"""  # Number of records
fun(query4)
query4 = """SELECT COUNT(DISTINCT MARKS) FROM STUDENT_records"""  # Prints number of disctinct marks
fun(query4)
query4 = """SELECT COUNT(NAMES) FROM STUDENT_records WHERE NAMES LIKE 'a%'"""  # Number of name starting with a
fun(query4)
query3 = """SELECT SUM(MARKS) FROM Student_records"""  # Finds sum of all marks
fun(query3)

input("Press Enter key to exit ")
