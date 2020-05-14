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

    def append(self,data):
        if(self.head==None):
            self.head = Node(data)
        new_head = Node(data)
        new_head.next = self.head.next
        self.head = new_head

    def end(self,data):
        end = Node(data)
        if (self.head == None):
            self.head = end
            return
        temp = self.head
        while(temp.next!=None):
            temp = temp.next        
        temp.next = end

    def mid(self,node,data):
        mid = Node(data)
        mid.next = node.next
        node.next = mid

    def deleting(self,data):
        temp = self.head
        if(temp.data!=None):
            if(temp.data==data):        
                self.head = temp.next
                temp = None            
                return

        while(temp!=None):
            if(temp.data==data):
                break
            prev = temp             
            temp = temp.next
        
        if(temp == None):
            return
        prev.next = temp.next
        temp = None                

print()

sll = LinkedList()

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


