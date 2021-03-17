class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printing(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next


# Creation
x = LinkedList()
x.head = Node("Red")  # First node
data2 = Node("Green")  # Filling Data Values for each node.
data3 = Node("Blue")

x.head.next = data2  # Head now points to data2
data2.next = data3  # data2 now points to data3

# Traversal
print()
x.printing()
