from tkinter import *
import tkinter
import socket
from threading import Thread

def receive():
    while (True):
        try:
            message = s.recv(1024).decode("utf8")
            message_list.insert(tkinter.END,message)
        except:
            print("ERROR : Unable to Recieve messages")
            break



window = Tk()
window.title("Chat Room")
window.configure(bg="white")

message_frame = Frame(window,height=100,width=100,bg="black")

my_message = StringVar()
my_message.set("")

scroll_bar = Scrollbar(message_frame)

message_list = Listbox(message_frame,height = 15,width = 100,bg = "black", yscrollcommand=scroll_bar.set)

scroll_bar.pack(side=RIGHT,fill=Y)
message_list.pack(side=LEFT,fill=BOTH)
message_frame.pack()

button_label = Label(window,text = "Enter Your Message",fg="black",bg="white")
button_label.pack()

text_field = Entry(window,textvariable=my_message, fg="black", bg="white",width = 50)
text_field.pack()

send_button = Button(window,text = "Send", bg="white",fg="black", command = send)
send_button.pack()

quit_button = Button(window,text = "Exit", bg="white",fg="black", command = closing)
quit_button.pack()

window.protocol("WM_DELETE_WINDOW",closing)

host = "192.168.0.192"; port = 8080
s = socket.socket()
s.connect((host,port))
recieve_thread = Thread(target=receive)
recieve_thread.start()

mainloop()