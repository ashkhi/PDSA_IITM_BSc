class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return bool(self.value)

    def printList(self):
        node = self.head
        while(node):
            print(node.value)
            node = node.next

def reverse(root):
    previousNode = None
    currentNode = root.head
    while(currentNode is not None):
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    root.head = previousNode
    return root

l = LinkedList()
a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

l.head = a
a.next = b
b.next = c
c.next = d
d.next = e

reverse(l).printList()