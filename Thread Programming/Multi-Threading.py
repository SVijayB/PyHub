from threading import Thread
import threading

def Numbers():
    print(threading.current_thread().getName(),"Has started")
    for x in range(10):
        print(x)

    print(threading.current_thread().getName(),"Has stopped")
    
    print("\nYou can see that both the functions ran parallely")
t1 = Thread(target=Numbers)
t2 = Thread(target=Numbers)
t1.start()
t2.start()