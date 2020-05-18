import socket
print("Run the Server and the Client through command prompt using \"python filename.py\"",
"from the Socket Programming directory or by just directly double tapping the script files")
s = socket.socket()
host = "localhost"; port = 8080
s.connect((host,port))
path = "assets/"
x = input("Enter the name of the file you want to read : ")
fileName = (path+x)
s.send(fileName.encode())
info = s.recv(1024)     # Getting the info from the file.
print(info.decode())
s.close()
input("Press any key to exit ")

 