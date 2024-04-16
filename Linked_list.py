# Singly Linked List
'''
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        
n1=Node(3)
n2=Node(5)
n3=Node(8)
n4=Node(23)

n1.next=n2
n2.next=n3
n3.next=n4

current_node=n1
while current_node:
    print(current_node.data , end="->")
    current_node=current_node.next
print("Null")

# Doubly Linked List :

class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        self.prev=None
        
n1=Node(3)
n2=Node(5)
n3=Node(8)
n4=Node(23)

n1.next=n2
n2.prev=n1

n2.next=n3
n3.prev=n2

n3.next=n4
n4.prev=n3


current_node=n1
print(" \n Traverse Forward:")
while current_node:
    print(current_node.data , end="->")
    current_node=current_node.next
print("Null")

current_node=n4
print(" \n Tranverse Backword :")
while current_node:
    print(current_node.data , end="->")
    current_node=current_node.prev
print("Null")
print()
      
# Circular Linked List

class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        
        
n1=Node(3)
n2=Node(5)
n3=Node(8)
n4=Node(23)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n1

current_node=n1
start_node=n1

print(current_node.data , end="->")
current_node=current_node.next

while current_node != start_node:
    print(current_node.data , end="->")
    current_node=current_node.next
print("....")

# Doubly Circular Linked List

class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        self.prev=None
        
n1=Node(3)
n2=Node(5)
n3=Node(8)
n4=Node(23)

n1.next=n2
n2.prev=n1

n2.next=n3
n3.prev=n2

n3.next=n4
n4.prev=n3

n4.next=n1
n1.prev=n4

current_node=n1
start_node=n1
print(" \n Traverse Forward:")
print(current_node.data , end="->")
current_node=current_node.next

while current_node != start_node:
    print(current_node.data,end='->')
    current_node=current_node.next
print("....")


current_node=n4
start_node=n4
print(" \n Tranverse Backword :")
print(current_node.data,end='-->')
current_node=current_node.prev

while current_node != start_node:
    print(current_node.data , end="->")
    current_node=current_node.prev
print("....")
print()

# Traverse Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    def TraverseAdd(head):
        current_node=head
        while current_node:
            print(current_node.data,end='->')
            current_node=current_node.next
        print("Null")

n1=Node(6)
n2=Node(32)
n3=Node(12)
n4=Node(7)
n5=Node(9)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n1.TraverseAdd()

# Lowest Value

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    def lowest_value(head):
        minvalue=head.data
        current_node=head.next
        while current_node:
            if current_node.data < minvalue:

              minvalue=current_node.data
            current_node=current_node.next
        return minvalue
n1=Node(62)
n2=Node(32)
n3=Node(12)
n4=Node(7)
n5=Node(9)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n1.lowest_value() 
print(n1.lowest_value())'''

# Deletinh Node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traverse(head):
        current_node=head
        while current_node:
            print(current_node.data,end="->")
            current_node=current_node.next
        print("Null")

    def deleteSpecificNode(head, nodeToDelete):

     if head == nodeToDelete:
        return head.next

     currentNode = head
     while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

     if currentNode.next is None:
        return head

     currentNode.next = currentNode.next.next

     return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
#traverseAndPrint(node1)
node1.traverse()
print(node1.traverse())

# Delete node4

#node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
node1.deleteSpecificNode(node1)
node4.deleteSpecificNode(node4)
print(node1.traverseAndPrint())
print(node4.traverseAndPrint())