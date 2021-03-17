class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.Prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        if self.head != None:
            self.head.prev = temp
        self.head = temp

    def printing(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def delete(self, node):
        if node.prev == None:
            self.x = node.next
        else:
            node.prev.next = node.next

        if node.next == None:
            self.y = node.prev
        else:
            node.next.prev = node.prev


dll = DoublyLinkedList()
dll.add("Blue")
dll.add("Red")
dll.add("Green")
dll.delete(dll.head.next)
dll.printing()
