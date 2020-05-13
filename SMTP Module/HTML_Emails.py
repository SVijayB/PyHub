import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"    
port = 587                  

username = str(input("Enter Gmail Username : "))                                
password = str(input ("Enter Gmail Password"))                                           
message = "Hey there! I sent this MAIL using Python's SMTP module"  
_to = [username]            # Add any other username you want by adding a comma.                
_from = username
try:
    connection = smtplib.SMTP(host,port)
    connection.ehlo()
    connection.starttls()
    connection.login(username,password)         
    print("\nCONNECTION SUCCESSFUL")
    connection.sendmail(_from,_to,message)      
    print("Message has been sent Successfully")
    connection.quit()                           
    print("Connection has been closed.")
    tmessage = MIMEMultipart("alternate")           # For the mail to understand HTML
    tmessage ["Subject"] = "Html Message"           # You can add Subjects as well.
    message[]
except:
    print("CONNECTION ERROR")