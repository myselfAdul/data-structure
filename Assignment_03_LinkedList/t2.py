# Task - 02

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


def remove_compartment(head, n):
    # TO DO
    current = head
    length = 0
    # finding the length of the linked list
    while current is not None:
        length += 1
        current = current.next

    # when not doable
    if length < n:
        return head

    # Link start
    start = length - n

    # remove the 1st element
    if start == 0:
        head = head.next
        return head

    # remove any element
    l = 0
    current = head
    while current is not None:
        l += 1
        if l == start:
            current.next = current.next.next

        current = current.next

    return head


print("==============Test Case 1=============")
head = createList(np.array([10, 15, 34, 41, 56, 72]))
print("Original Compartment Sequence: ", end=" ")
printLinkedList(head)
head = remove_compartment(head, 2)
print("Changed Compartment Sequence: ", end=" ")
printLinkedList(head)  # This should print 10-->15-->34-->41-->72
print()


print("==============Test Case 2=============")
head = createList(np.array([10, 15, 34, 41, 56, 72]))
print("Original Compartment Sequence: ", end=" ")
printLinkedList(head)
head = remove_compartment(head, 7)
print("Changed Compartment Sequence: ", end=" ")
printLinkedList(head)  # This should print 10-->15-->34-->41-->56-->72
print()

print("==============Test Case 3=============")
head = createList(np.array([10, 15, 34, 41, 56, 72]))
print("Original Compartment Sequence: ", end=" ")
printLinkedList(head)
head = remove_compartment(head, 6)
print("Changed Compartment Sequence: ", end=" ")
printLinkedList(head)  # This should print 15-->34-->41-->56-->72
print()
