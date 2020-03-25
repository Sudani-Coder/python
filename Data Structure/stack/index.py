from sys import maxsize

class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def push(self, item):
        self.items.append(item)
        print(str(item) + " pushed to stack ") 

    def pop(self):
        if (self.isEmpty()):
            raise IndexError("the stack is empty")
        return self.items.pop()

MyStack = stack()
MyStack.push(19)
MyStack.push(16)
MyStack.push(12)
print(MyStack.items)
MyStack.pop()
print(MyStack.items)
MyStack.pop()
MyStack.pop()
print(MyStack.items)
MyStack.pop()
