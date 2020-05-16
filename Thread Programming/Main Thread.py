import threading 

# Checking if main thread or not
t = threading.current_thread().getName()
if threading.current_thread()==threading.main_thread():
    print("This is a main thread")
else:
    print("Not a main thread")
print(t)
threading.current_thread().name = "MAIN THREAD!"        # Changing the name of the main thread
print(threading.current_thread().getName())