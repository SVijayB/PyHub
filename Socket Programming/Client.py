import socket

s = socket.socket()
host = "localhost"
port = 8080
try:
    s.connect((host, port))  # Always pass as tuple
    message = s.recv(
        1024
    )  # Messages received will be saved in variable message and byte is max 1024
    while message:
        print("Message :", message.decode())  # Decoding the encoded message received
        message = s.recv(
            1024
        )  # Loop keeps decoding and storing it into message variable.
    s.close()  # Closed connection.
except:
    print("ERROR : MAKE SURE THE SERVER IS RUNNING")
input("Press Enter key to exit ")
