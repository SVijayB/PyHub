"""
In the flight reservation program, we used sleep function to prevent the threads from running at once.
However, the more efficient method to do this would be by using the build in class "Lock".
"""
from threading import *
from time import sleep

class flightReservation:
    l = Lock()
    def __init__(self,ticket_left):
        self.ticket_left = ticket_left
    l.acquire()
    def buy(self,ticketRequest):
        if(self.ticket_left>=ticketRequest):
            print("Your tickets are confirmed")
            print("Make payment and collect tickets")
            self.ticket_left -= ticketRequest
        else:
            print("Sorry, not enough tickets remaining")
    l.release()
res = flightReservation(8)
t1 = Thread(target=res.buy,args=[3])
t2 = Thread(target=res.buy,args=[4])
t3 = Thread(target=res.buy,args=[7])
t1.start()
t2.start()
t3.start()
"""
If you noticed in this case, it prints the else statement. 
This is because, the processes are ran one after another.
"""