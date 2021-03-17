from threading import Thread
import threading
from time import sleep


def Numbers():
    print(threading.current_thread().getName(), "Has started")
    for x in range(10):
        print(x)

    print(threading.current_thread().getName(), "Has stopped")


t1 = Thread(target=Numbers)
t2 = Thread(target=Numbers)
t1.start()
sleep(
    2
)  # Using sleep function to prevent parallel threading from collapsing each other.
t2.start()
sleep(2)
print("\nYou can see that both the functions ran parallely")
sleep(1)
input("Enter any Key to exit ")
