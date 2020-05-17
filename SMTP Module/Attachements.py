import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

host = "smtp.gmail.com"    
port = 587                  

username = str(input("Enter Gmail Username : "))                                
password = str(input ("Enter Gmail Password : "))                                           
_to = username                                      # Add any other username you want by adding a comma.                
_from = username
try:
    connection = smtplib.SMTP(host,port)
    connection.ehlo()
    connection.starttls()
    connection.login(username,password)         
    print("\nCONNECTION SUCCESSFUL")

    message = MIMEMultipart("alternate")           # For the mail to understand HTML
    message ["Subject"] = "Html Message"           # You can add Subjects as well.
    message["From"] = _from
    message["To"] = _to
    
    html_message =  """
    <html>
        <body>
            <h3>ATTACHMENT</h3>
            <p>Hey! This Email contains an Attachment file.</p>
        </body>
    </html>
                    """
    msg = MIMEText(html_message,"html")
    message.attach(msg)

    filename = "Mail Attachments/name.txt"              # File path.
    openfile = open(filename,'rb')                      # Opening the file.
    mimref = MIMEBase("applicaiton","octect_stream")    # Telling the browser the way to open the file.
    mimref.set_payload(openfile.read())                 # Setting the file as payload to be sent.
    encoders.encode_base64(mimref)                      # Mail has to be encoded.
    mimref.add_header("Content-Disposition","openfile;filename=name.txt")   # Setting attachmenet name and type.
    message.attach(mimref)                              # Attaching the file.

    connection.sendmail(_from,_to,message.as_string())      
    print("Message has been sent Successfully")
    connection.quit()                           
    print("Connection has been closed.")
except:
    print("CONNECTION ERROR")
    print("PROGRAM TERMINATED")