from threading import Thread
import threading

class MyThread(Thread):
    def run(self):
        print("Pyramid : ")
        print(threading.current_thread().getName())
        for x in range(0,5):
            for j in range(0,x+1):
                print("*",end=" ")
            print("\r")

obj = MyThread()
obj.start()         # Part of the thread we created. From the inherited class of Thread.

"""
class MyThread(Thread):
    def run(self):
        print("Pyramid : ")
        print(threading.current_thread().getName())
        for x in range(0,5):
            for j in range(0,x+1):
                print("*",end=" ")
            print("\r")

obj = MyThread()
obj.run()         # Main thread since not part of the class. 
# You can also notice that the pattern is not formed properly. This is because both the codes run parallely
"""