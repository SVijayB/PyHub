class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

# Inserting at the beginning : 
    def add(self,data):
        temp = Node(data)
        temp.next = self.head
        if(self.head!=None):
            self.head.prev = temp
        self.head = temp 

# Inserting after a Node :
    def insertion(self,node,data):
        temp = Node(data)
        temp.next = node.next
        node.next = temp
        temp.prev = node
        if (temp.next!=None): 
            temp.next.prev = temp

# Inserting at the last Node:
    def end(self,data):
        new = Node(data)
        temp = self.head
        new.next = None
        if (self.head == None):
            new.prev = None
            self.head = new
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = new
        new.prev = temp 

    def printing(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next

print()
dll = DoubleLinkedList()
dll.add("Red")
dll.add("Yellow")
dll.insertion(dll.head.next,"Blue")
dll.end("Green")
dll.printing()