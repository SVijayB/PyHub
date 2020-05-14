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

    def append(self,data4):
        new_head = Node(data4)
        new_head.next = self.head.next
        self.head = new_head

    def end(self,data5):
        end = Node(data5)
        if (self.head == None):
            self.head = end
            return
        temp = self.head
        while(temp.next!=None):
            temp = temp.next        
        temp.next = end

    def mid(self,node,data6):
        mid = Node(data6)
        mid.next = node.next
        node.next = mid

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

sll.head.next = data2
data2.next = data3

sll.append("Yellow")
sll.end("Purple")
sll.mid(sll.head.next,"Orange")
sll.mid(sll.head.next.next,"Pink")
sll.printing()

sll.deleting("Blue")
sll.deleting("Green")
sll.deleting("Purple")

print("\nAFTER DELETING : ")
sll.printing()


