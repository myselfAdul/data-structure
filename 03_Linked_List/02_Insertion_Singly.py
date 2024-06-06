class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        pass


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

head = node1
current = head

while current is not None:
    print(current.data, end="->")
    current = current.next
    if current == None:
        print(None)
    pass

#  Insert in beginning
new_node = Node(5)
new_node.next = head
head = new_node
current = head

print("\nAfter inserting at begining:\n====================")

# Print the list
while current:
    print(current.data, end="->")
    current = current.next

    if current is None:
        print(None)
    pass


# insert in end:
print("\nAfter inserting at end:\n====================")
new_node = Node(50)
head = node1
current = head

while current.next is not None:
    current = current.next
current.next = new_node

head = node1
current = head

# Print the list
while current:
    print(current.data, end="->")
    current = current.next
    if current == None:
        print(None)
    pass


# insert after 20
print("\nInserting after 20 :\n====================")

head = node1
current = head

new_node = Node(22)
while current is not None and current.data != 20:
    current = current.next
    pass

new_node.next = current.next
current.next = new_node

head = node1
current = head

# Print the list
while current:
    print(current.data, end="->")
    current = current.next
    if current == None:
        print(None)
    pass
