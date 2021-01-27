import secrets
import string
import sys
import sqlite3

def random_password_generation():
    alphabet = string.ascii_letters + string.digits
    password = ""
    for i in range(10):
        password = password + ''.join(secrets.choice(alphabet)) 
    print("Randomly generated password -> ", password)
    return password

def save_password(username, user_password, random_password):
    connection = sqlite3.connect("Account_details.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Account(USERNAME,USER_PASSWORD,RANDOM_PASSWORD)VALUES(?,?,?)""",(username,user_password,random_password))
    connection.commit()
    connection.close()
    print("Values have been successfully stored in the database")

if __name__ == "__main__":
    try:
        database = sqlite3.connect("Account_details.db")
        database.execute("""CREATE TABLE Account(USERNAME TEXT NOT NULL, 
        USER_PASSWORD TEXT NOT NULL, RANDOM_PASSWORD TEXT NOT NULL)""")
    except:
        pass

    user_password = "abcd1234"
    username = str(input("Please enter your User name \n> "))
    user_entered_password = str(input("Please enter your password \n> "))
    if(user_password == user_entered_password):
        print("Password matched!")
        random_password = random_password_generation()
        save_password(username, user_entered_password, random_password)
        input("Press enter key to exit")
    else:
        print("You have entered the wrong password. Please verify...")
        save_password(username, user_entered_password, "NULL")
        input("Press enter key to exit")
        sys.exit(0)