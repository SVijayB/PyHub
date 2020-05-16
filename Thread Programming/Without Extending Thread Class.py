import threading
from threading import Thread

class MyThread:
    def numbers(self):
        print("\n"+threading.current_thread().getName())
        for x in range (1,10):
            print(x)

object = MyThread()
t = Thread(target=object.numbers)
t.start()