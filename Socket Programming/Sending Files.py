# This is a server that sends files over to the client that requests for the file.
import socket

s = socket.socket()
host = "localhost"; port = 8080
s.bind((host,port))
s.listen(1)
print("The server is online at port",port)
con,address=s.accept() 
print("Connection has been made from " + str(address))
try:
    fileName = con.recv(1024)
    file = open(fileName,'rb')     # Opening the file in read mode.
    readFile = file.read()         # Saving info from file in variable readFile
    con.send(readFile)             # Sending the info present in the file
    con.close()
except:
    con.send("File not found in server. Recheck name and format".encode())
    con.close()