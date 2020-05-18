import socket
from threading import Thread
clients = {}
addresses = {}
host = "192.168.0.192"; port = "8080"

s = socket.socket()
s.bind((host,port))

def accept_client():
    while (True):
        client_con,client_address=s.accept()
        print(client_address, "Has Connected")

if __name__ == "__main__":
    s.listen(5)         # Only 5 clients can join
    print("The Server Is Now Online")
    t1 = Thread(target=accept_client)
    t1.start()
    t1.join()           # Waits for one thread to stop before running the next.