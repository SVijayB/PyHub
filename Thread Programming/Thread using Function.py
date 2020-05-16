from threading import Thread
import threading

def evenNumber():
    for x in range (20):
        if x%2 == 0:
            print(x)

t = Thread(target=evenNumber)
t.start()
