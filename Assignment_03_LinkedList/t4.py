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


# def word_Decoder(head):
#     current = head
#     length = 0
#     # finding the length of the linked list
#     while current is not None:
#         length += 1
#         current = current.next

#     key = 13 % length

#     c = -1

#     current = head

#     dummy = Node("None")

#     while current:
#         c += 1
#         if c % key != 0:
#             dummy.next = current.next

#         current = current.next
#     return dummy


def word_Decoder(head):
    # Calculate the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Calculate the position factor
    position_factor = 13 % length

    # Collect letters at multiples of position_factor
    letters = []
    current = head
    index = 0
    while current:
        if index != 0 and index % position_factor == 0:
            letters.append(current.elem)
        current = current.next
        index += 1
    # print(letters)

    # Reverse the collected letters
    reversed_letters = []
    for i in range(len(letters) - 1, -1, -1):
        reversed_letters.append(letters[i])

    # Create a new linked list with a dummy head node
    dummy_head = Node(None)
    current = dummy_head
    for letter in reversed_letters:
        current.next = Node(letter)
        current = current.next

    return dummy_head


# Driver Code
print("==============Test Case 1=============")
head = createList(np.array(["B", "M", "D", "T", "N", "O", "A", "P", "S", "C"]))
print("Encoded Word:")
printLinkedList(head)  # This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)  # This should print None→C→A→T

print("==============Test Case 2=============")

head = createList(np.array(["Z", "O", "T", "N", "X"]))
print("Encoded Word:")
printLinkedList(head)  # This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)  # This should print None→N
