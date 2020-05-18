import socket
from threading import Thread
clients = {}
addresses = {}
host = "192.168.0.192"; port = 8080

s = socket.socket()
s.bind((host,port))

def accept_client():
    while (True):
        client_con,client_address=s.accept()
        print(client_address, "Has Connected")
        client_con.send("Hey! Welcome to the Chat Room. Enter Your Name To Continue.".encode("utf8"))
        addresses[client_address] = client_address
        t2 = Thread(target=handle_client,args=(client_con,client_address))
        t2.start()
    

def handle_client(con,adr):
    name = con.recv(1024).decode("utf8")
    welcome = "Thanks for using this Chat Room " + name + ". You can use #quit if you want to exit"
    con.send(bytes(welcome,"utf8"))

    message = name + " has joint the chat!"
    broadcast(bytes(message,"utf8"))

    clients[con] = name

    while(True):
        message = con.recv(1024)
        if(message!=bytes("#quit","utf8")):
            broadcast(message, name + ":")
        else:
            con.send(bytes("#quit","utf8"))
            con.close()
            del clients[con]
            broadcast(bytes(name + " has left the chat."))


def broadcast(message,prefix=""):
    for x in clients:
        x.send(bytes(prefix,"utf8")+message)


if __name__ == "__main__":
    s.listen(5)         # Only 5 clients can join
    print("The Server Is Now Online")
    t1 = Thread(target=accept_client)
    t1.start()
    t1.join()           # Waits for one thread to stop before running the next.