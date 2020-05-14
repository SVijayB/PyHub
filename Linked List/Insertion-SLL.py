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

# Appending -> Making the added element the head.
    def append(self,data4):
        new_head = Node(data4)
        new_head.next = self.head
        self.head = new_head

sll = LinkedList()
sll.head = Node("Blue")
data2 = Node("Red")
data3 = Node("Green")

sll.head.next = data2
data2.next = data3

sll.append("Yellow")
sll.printing()


