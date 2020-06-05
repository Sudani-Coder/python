class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def append(self, NewNode):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            else:
                current.next = NewNode
        else:
            self.head = NewNode

    def insertFirst(self, NewNode):
        NewNode.next = self.head
        self.head = NewNode

    def deleteFirst(self):
        if self.head:
            deletedNode = self.head
            temp = deletedNode.next
            self.head = temp
            return deletedNode
        
        else:
            return None

class Stack:
    def __init__(self, top = None):
        self.LL = LinkedList(top)

    def push(self, NewNode):
        self.LL.insertFirst(NewNode)

    def pop(self):
        return self.LL.deleteFirst()

# Test cases
# Set up some Elements
e1 = Node(2)
e2 = Node(4)
e3 = Node(8)
e4 = Node(16)

# Start setting up a Stack
stack = Stack()
print(stack, end = "\n\n")
print(stack.LL, end = "\n\n")
print(stack.LL.head, end = "\n\n")

# Test stack functionality
stack.push(e1)
print(e1, e1.data, e1.next, sep = " => ", end = "\n\n")

stack.push(e2)
print(e2, e2.data, e2.next, sep = " => ", end = "\n\n")

stack.push(e3)
stack.push(e4)

print(stack)
