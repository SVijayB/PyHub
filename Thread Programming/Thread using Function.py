from threading import Thread
import threading
from time import sleep

def evenNumber():
    a = threading.current_thread().getName()
    print("Thread Inside the function :",a)
    threading.current_thread().name = "Even Number Thread"
    print("After changing thread name",threading.current_thread().getName())
    for x in range (20):
        if x%2 == 0:
            print(x)

a = threading.current_thread().getName()
print("\nThread outside the function : "+a)
t = Thread(target=evenNumber)
t.start()
sleep(1)
input("Enter any Key to exit ")

