from threading import Thread
import threading

def evenNumber():
    a = threading.current_thread().getName()
    print("Thread Inside the function :",a)
    for x in range (20):
        if x%2 == 0:
            print(x)

a = threading.current_thread().getName()
print("\nThread outside the function : "+a)
t = Thread(target=evenNumber)
t.start()

