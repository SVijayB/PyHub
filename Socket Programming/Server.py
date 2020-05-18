# Creating a server that takes client requests.
import socket
host = "localhost"; port = 8080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    # 1st arg -> IPv4, 2nd arg -> TCP connection.
# The two above args are present by default. You need not mention it if you don't want to.
s.bind((host,port))         # Always pass as tuple.
s.listen(1)                 # Server is listening -> arg is for no. of connections the server allows.
print("The server is online at port",port)
con,address=s.accept()      # Connection -> con and address from where it is connected -> address
print("Connection has been made from " + str(address))
con.send("Hey! You have successfully connected to the server".encode())     # Make sure you encode messages.
con.close()