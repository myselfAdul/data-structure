class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        pass

    pass


# create Node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# connect Node
node1.next = node2
node2.next = node3
node3.next = node4

# print Linked List
head = node1
print(f"Head: {head.data}")

current = head
while current:
    # print(f"{current.data}->")
    print(current.data, end="->")
    current = current.next
    if current is None:
        print("Null")
        pass
