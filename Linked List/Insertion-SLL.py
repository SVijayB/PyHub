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
        new_head.next = self.head.next
        self.head = new_head

# Insertion at End
    def end(self,data5):
        end = Node(data5)
        if (self.head == None):
            self.head = end
            return
        temp = self.head
        while(temp.next!=None):
            temp = temp.next        # Iterates until the last node
        temp.next = end

# Insertion in the middle
    def mid(self,node,data6):
        mid = Node(data6)
        mid.next = node.next
        node.next = mid

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


