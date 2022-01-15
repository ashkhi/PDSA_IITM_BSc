'''class Node:
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

def insertAt(head, value, x):
    if(x == 0):
        print("at beg")

    pos = head
    i = 1
    while(pos!=None and i<x):
        pos = pos.next
        i+=1

    if(i==x):
        temp = pos.next
        pos.next = Node(value)
        pos.next.next = temp
    else:
        raise Exception("No")

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
insertAt(l, 60, 1)
l.printList()'''


'''a = [1,2,3]
a.insert(0,4)
print(a)
a.pop()
print(a)'''


def partition(a, low, up):
    i = low+1
    j = up
    pivot = a[low]

    while(i <=j):
        while(a[i]<pivot and i<up):
            i+=1
        while(a[j]>pivot):
            j-=1
        if(i<j):
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
        else:
            i+=1
    a[low] = a[j]
    a[j] = pivot
    return j

arr = [13, 18, 8, 10, 21, 7, 2, 32, 6, 19]
temp = partition(arr, 0, 9)
print(arr)