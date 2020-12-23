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
        return self.items[-1]

    def push(self, item):
        self.items.append(item)
        return item

    def pop(self):
        if (self.isEmpty()):
            raise IndexError("the stack is empty")

        else:
            return self.items.pop()

    def printStack(self):
        return self.items

    def size(self):
        return len(self.items)
