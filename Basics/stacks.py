stack = []


def isEmpty(stack):
    if stack == []:
        return True
    else:
        return False
def push(stack):
    item = int(input("enter value"))
    stack.append(item)
    top = len(stack)-1
def pop(stack):
    if isEmpty(stack):
        print("underflow")
    else:
        item=stack.pop()
        if len(stack) == 0:
            top = None
        else:
            top = len(stack)-1
        print(item,"is deleted")
def peek(stack):
    if isEmpty(stack):
        print("stack empty")
    else:
        top = len(stack)-1
        print(stack[top])
def display(stack):
    if isEmpty(stack):
        print("stack empty")
    else:
        top = len(stack)-1
        for a in range(top,-1,-1):
            print(stack[a])
while True:
    menu = int(input('1.push\n 2.pop\n 3.peek\n 4.display'))
    if menu == 1:
        push(stack)
        print("\n")
    elif menu == 2:
        pop(stack)
    elif menu == 3:
        peek(stack)
    elif menu == 4:
        display(stack)
    else:
        break
# credits Nishchal github ID(Nish251103)