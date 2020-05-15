import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        insert = Node(data)
        temp = self.head
        while(temp.next!=None):
            if(temp.data==node):
                break
            temp = temp.next
        temp.next = insert
        temp.prev = temp
        if (insert.next!=None): 
            temp.next.prev = insert

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

# Deleting
    def delete(self,node):
        temp = self.head
        while(temp.next!=None):
            if(temp.data==node):
                break
            temp = temp.next
        if (temp.prev == None):
            self.x = temp.next
        else:
            temp.prev.next = temp.next
        
        if(temp.next == None):
            self.y = temp.prev
        else:
            temp.next.prev = temp.prev

# Printing
    def printing(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next

dll = DoublyLinkedList()

while(True):
    try:
        print("\nWhat would you like to do?")
        print("1. Add an Element")
        print("2. Delete an Element")
        print("3. Print Linked List")
        print("4. Close the Progream")
        choice = int(input("Choose between 1,2,3 or 4 : "))
        if(choice!=1 and choice!=2 and choice!=3 and choice!=4):
            raise ValueError
    except ValueError:
        print("\nERROR : ONLY VALUE BETWEEN 1-4 IS ACCEPTED")
    else:
        if(choice==1):
            try:
                print("\nWhere would you like to insert new Element?")
                print("1. First Position")
                print("2. Last Poisition")
                print("3. Between two Nodes")
                ans = int(input("Choose between 1,2 or 3 : "))
                if(ans!=1 and ans!=2 and ans!=3):
                    raise ValueError
            except ValueError:
                print("\nERROR : ONLY VALUE BETWEEN 1-3 IS ACCEPTED")
            else:
                if(ans==1):
                    data = str(input("Enter Data to be stored in the first position : "))
                    dll.add(data)
                if(ans==2):
                    data = str(input("Enter Data to be stored in the last position : "))
                    dll.end(data)
                if(ans==3):
                    dll.printing()
                    data = str(input("\nEnter Data to be stored in between two nodes : "))
                    nodeinfo = str(input("Enter after which node you want to insert : "))
                    dll.insertion(nodeinfo,data)           
        if(choice==2):
            dll.printing()
            data = str(input("\nWhich Element do you want to delete? : "))
            dll.delete(data)

        if(choice==3):
            dll.printing()

        if(choice==4):
            sys.exit(0)

