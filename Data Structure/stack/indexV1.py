# Stack data structure
# Add three operation's to the stack (test stack if isEmpty)
# Push items to stack and delete items form stack

# Stack class blue print
class Stack:

    # Function to initialise the stack object 
    def __init__(self):
        self.items = [] # Initialize stack object as null

    # Function return True boolean value if stack is empty
    def isEmpty(self):
        return (self.items == [])

    def peek(self):
        print(self.items[-1])

    def push(self, item):
        self.items.append(item)
        print(str(item) + " pushed to stack ")

    def pop(self):
        if (self.isEmpty()):
            raise IndexError("the stack is empty")

        else:
            print(f"{self.items.pop()} poped from stack")

    def printStack(self):
        print(self.items)

    def size(self):
        print(f"The size of stack is {len(self.items)}")

MyStack = Stack()

MyStack.push(19)
MyStack.push(16)
MyStack.push(12)
MyStack.push(8)

MyStack.peek()
MyStack.printStack()
MyStack.size()

MyStack.pop()
MyStack.peek()
MyStack.pop()

MyStack.printStack()
MyStack.size()
MyStack.peek()
