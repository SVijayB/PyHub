import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587

username = str(input("Enter Gmail Username : "))
password = str(input("Enter Gmail Password : "))
_to = username  # Add any other username you want by adding a comma.
_from = username
try:
    connection = smtplib.SMTP(host, port)
    connection.ehlo()
    connection.starttls()
    connection.login(username, password)
    print("\nCONNECTION SUCCESSFUL")

    tmessage = MIMEMultipart("alternate")  # For the mail to understand HTML
    tmessage["Subject"] = "Html Message"  # You can add Subjects as well.
    tmessage["From"] = _from
    tmessage["To"] = _to

    html_message = """
    <html>
        <body>
            <h1>HTML MESSAGE</h1>
            <p>Hey! This is a HTML Message</p>
        </body>
    </html>
                    """
    msg = MIMEText(html_message, "html")
    tmessage.attach(msg)

    connection.sendmail(_from, _to, tmessage.as_string())
    print("Message has been sent Successfully")
    connection.quit()
    print("Connection has been closed.")
except:
    print("CONNECTION ERROR")
    print("PROGRAM TERMINATED")
