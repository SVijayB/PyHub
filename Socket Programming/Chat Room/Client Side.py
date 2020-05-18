from tkinter import *
import tkinter
import socket
from threading import Thread

window = Tk()
window.title("Chat Room")
window.configure(bg="black")

message_frame = Frame(window,height=100,width=100,bg="white")

my_message = StringVar()
my_message.set("")

scroll_bar = Scrollbar(message_frame)

message_list = Listbox(message_frame,height = 15,width = 100,bg = "white", yscrollcommand=scroll_bar.set)

scroll_bar.pack(side=RIGHT,fill=Y)
message_list.pack(side=LEFT,fill=BOTH)
message_frame.pack()
mainloop()