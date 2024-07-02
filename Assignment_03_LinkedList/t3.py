# Task - 03

import numpy as np
import fhm_unittest as unittest


# Run this cell
class Node:
    def __init__(self, elem, next=None):
        self.elem, self.next = elem, next


def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
    return head


def printLinkedList(head):
    temp = head
    while temp != None:
        if temp.next != None:
            print(temp.elem, end="-->")
        else:
            print(temp.elem)
        temp = temp.next
    print()


def assemble_conga_line(conga_line):
    # TO DO
    current = conga_line
    while current is not None and current.next is not None:
        if current.elem > current.next.elem:
            return "False"
        current = current.next
    return "True"


print("==============Test Case 1=============")
conga_line = createList(np.array([10, 15, 34, 41, 56, 72]))
print("Original Conga Line: ", end=" ")
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value)  # This should print True
unittest.output_test(returned_value, True)
print()

print("==============Test Case 2=============")
conga_line = createList(np.array([10, 15, 44, 41, 56, 72]))
print("Original Conga Line: ", end=" ")
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value)  # This should print False
unittest.output_test(returned_value, False)
print()
