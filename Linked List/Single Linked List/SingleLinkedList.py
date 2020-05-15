import sys

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printing(self):
        print("\nElements in Linked List are : ")
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next

    def append(self,data):
        new_head = Node(data)
        new_head.next = self.head
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
        temp = self.head
        while(temp.next!=None):
            if(temp.data==node):
                break
            temp = temp.next
        mid = Node(data)
        mid.next = temp.next
        temp.next = mid

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

sll = LinkedList()

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
        print("ERROR : ONLY VALUE BETWEEN 1-4 IS ACCEPTED")
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
                print("ERROR : ONLY VALUE BETWEEN 1-3 IS ACCEPTED")
            else:
                if(ans==1):
                    data = str(input("Enter Data to be stored in the first position : "))
                    sll.append(data)
                if(ans==2):
                    data = str(input("Enter Data to be stored in the last position : "))
                    sll.end(data)
                if(ans==3):
                    sll.printing()
                    data = str(input("\nEnter Data to be stored in between two nodes : "))
                    nodeinfo = str(input("Enter after which node you want to insert : "))
                    sll.mid(nodeinfo,data)           
        if(choice==2):
            sll.printing()
            data = str(input("\nWhich Element do you want to delete? : "))
            sll.deleting(data)

        if(choice==3):
            sll.printing()

        if(choice==4):
            sys.exit(0)



