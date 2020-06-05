# linkedlist data structure
# Add three functions to the LinkedList.
# get_position" returns the element at a certain position.
# The "insert" function will add an element to a particular spot in the list.
# delete" will delete the first element with that particular value.

# Node class 
class Node:

    # Function to initialise the node object 
    def __init__(self, data):
        self.data = data    # Assign data
        self.next = None    # Initialize next node as null

# LinkedList class
class LinkedList:
    
    # Function to initialize the Linked List object 
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        # function to check whether the list is empty
        return self.head == None

    def append(self, NewNode):
        """
        Append node at the end of linked list
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            
            current.next = NewNode
        
        else:
            self.head = NewNode

    def insert(self, NewNode, position):
        current_index = 0
        current = self.head
        if position > 0:
            while current and current_index < position:
                if current_index == position - 1:
                    NewNode.next = current.next
                    current.next = NewNode

                current = current.next
                current_index += 1
            
        elif position == 0:
            NewNode.next = self.head
            self.head = NewNode

    # Function to delete any node
    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if prev is None:
            self.head = current.next
        
        elif current:
            prev.next = current.next
            current.next = None

    def get_position(self, position):
        """
        Get an element from a particular position.
        Assume the first position is "0".
        Return "None" if position is not in the list.
        """
        current_index = 0
        current = self.head
        if position < 0:
            return None

        while current and current_index <= position:
            if current_index == position:
                return current.data
            
            current = current.next
            current_index += 1

        return None
    
    def print_list(self):
        Node = self.head
        while Node != None:
            print(Node.data, end = " => ")
            Node = Node.next


N1 = Node(8)
N2 = Node(2)
N3 = Node(4)
N4 = Node(10)
N5 = Node("omer")
N6 = Node("taha")

MyLinkedList = LinkedList()

MyLinkedList.append(N1)
MyLinkedList.append(N2)
MyLinkedList.append(N3)
MyLinkedList.append(N4)
MyLinkedList.append(N5)

MyLinkedList.insert(N6, 2)

print(MyLinkedList.get_position(0))

MyLinkedList.print_list()
