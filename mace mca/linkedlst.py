class Node:
    data = None
    nextNode = None
    prevNode = None

    def __init__(self, value):
        self.data = value
        self.nextNode = None
        self.prevNode = None

head = None 
n = int(input("Enter the no of nodes: "))
for _ in range(n):
    newnode = Node(input("Enter the new node value: "))
    if head == None:
        head = newnode
        currentNode = head
    else:
        currentNode.nextNode = newnode
        newnode.prevNode = currentNode
        currentNode = newnode
temp = head
temp1 = None
while(temp != None):
    print(temp.data, end=" ")
    temp1 = temp
    temp = temp.nextNode
print()

while(temp1!= None):
    print(temp1.data, end=" ")
    temp1 = temp1.prevNode
print()