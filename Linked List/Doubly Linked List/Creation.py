class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        a = Node(data)
        a.next = self.head
        if(self.head!=None):
            self.head.prev = a
        self.head = a 

    def printing(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next

print()
dll = DoublyLinkedList()
dll.add("Red")
dll.add("Blue")
dll.add("Green")
dll.add("Yellow")
dll.printing()
