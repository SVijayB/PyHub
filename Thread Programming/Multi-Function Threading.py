from threading import Thread
import threading
from time import sleep


def even_odd():
    print("Thread name when calling even_odd", threading.current_thread().getName())
    evenNo()  # Adding multiple functions
    oddNo()  # Adding a second function
    print(
        "\nIf you noticed, all of them have the same thread name, that is because the other two functions",
        "are called by the same function",
    )


def evenNo():
    print("Thread name when calling evenNo", threading.current_thread().getName())
    for x in range(10):
        if x % 2 == 0:
            print(x)


def oddNo():
    print("Thread name when calling oddNo", threading.current_thread().getName())
    for x in range(10):
        if x % 2 != 0:
            print(x)


t = Thread(target=even_odd)  # Function contains more than 1 function
t.start()
sleep(1)
input("Enter any Key to exit ")
