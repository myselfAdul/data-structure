# Task - 04

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


def sum_dist(head, arr):
    # TO DO
    sum = 0
    for i in arr:
        c = 0
        current = head
        while current:
            if c == i:
                sum += current.elem
                break
            c += 1
            current = current.next

    return sum


print("==============Test Case 1=============")
LL1 = createList(np.array([10, 16, -5, 9, 3, 4]))
dist = np.array([2, 0, 5, 2, 8])
returned_value = sum_dist(LL1, dist)
print(f"Sum of Nodes: {returned_value}")  # This should print Sum of Nodes: 4
unittest.output_test(returned_value, 4)
print()
