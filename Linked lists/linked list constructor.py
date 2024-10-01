class Node:
    def __init__(self,value) -> None: #since all the methods of the linked list need a new node, we create a new class that creates the new node
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self,value): #Create a node and initialize the linked list
        new_node = Node(value)
        self.head= new_node
        self.tail = new_node
        self.length=1

    def append(self,value):#create a new node and add the node to the end
        pass
    def prepend(self,value): #create a new node and add Node to the beginning
        pass
    def insert(self,value): #Create a node and insert it at an specific location
        pass

mylinkedlist = LinkedList(7)
print(mylinkedlist.length)
print(mylinkedlist.head.value)