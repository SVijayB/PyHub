import socket

s = socket.socket()
host = "localhost"; port = 8080
s.connect((host,port))
path = "Socket Programming/assets/"
x = input("Enter the name of the file you want to read : ")
fileName = (path+x)
s.send(fileName.encode())
info = s.recv(1024)     # Getting the info from the file.
print(info.decode())
s.close()

 