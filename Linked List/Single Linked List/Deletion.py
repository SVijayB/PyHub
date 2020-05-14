class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printing(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next

    def deleting(self,data):
        temp = self.head
        if(temp.data!=None):
            if(temp.data==data):        # Checks if first element is to be deleted
                self.head = temp.next
                temp = None             # Removing Garbage values.
                return

        while(temp!=None):
            if(temp.data==data):
                break
            prev = temp             # Node before the node to be deleted
            temp = temp.next
        
        if(temp == None):
            return
# temp.next points to the node after the node to be deleted. prev.next points to the to be deleted node.
        prev.next = temp.next
# Now, prev node points to the node after the node to be deleted.
        temp = None                 # Removing Garbage values.

print()
sll = LinkedList()
sll.head = Node("Blue")
data2 = Node("Red")
data3 = Node("Green")
data4 = Node("Yellow")

sll.head.next = data2
data2.next = data3
data3.next = data4
sll.deleting("Blue")
sll.deleting("Yellow")
sll.printing()