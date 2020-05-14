class Node:
    def __init__(self,datavalue=None):
        self.data = datavalue
        self.nextvalue = None

class LinkedList : 
    def __init__(self):
        self.headvalue = None

# Creation 
x = LinkedList()
x.headvalue = Node("Red")       # First node
data2 = Node("Green")           # Filling Data Values for each node.
data3 = Node("Blue")            

x.headvalue.nextvalue = data2   # Head now points to data2
data2.nextvalue = data3         # data2 now points to data3



