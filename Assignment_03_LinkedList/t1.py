# Task - 01

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


def check_similar(building_1, building_2):
    # TO DO
    current_1 = building_1
    current_2 = building_2

    while current_1 is not None and current_2 is not None:
        if current_1.elem == current_2.elem:
            current_1 = current_1.next
            current_2 = current_2.next

            if current_1 is None and current_2 is None:
                return "Similar"
            elif current_1 is None and current_2 is not None:
                return "Not Similar"
            elif current_2 is None and current_1 is not None:
                return "Not Similar"

        elif current_1.elem != current_2.elem:
            return "Not Similar"


print("==============Test Case 1=============")
building_1 = createList(np.array(["Red", "Green", "Yellow", "Red", "Blue", "Green"]))
building_2 = createList(np.array(["Red", "Green", "Yellow", "Red", "Blue", "Green"]))
print("Building 1: ", end=" ")
printLinkedList(building_1)
print("Building 2: ", end=" ")
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Similar'
unittest.output_test(returned_value, "Similar")
print()


print("==============Test Case 2=============")
building_1 = createList(np.array(["Red", "Green", "Yellow", "Red", "Yellow", "Green"]))
building_2 = createList(np.array(["Red", "Green", "Yellow", "Red", "Blue", "Green"]))
print("Building 1: ", end=" ")
printLinkedList(building_1)
print("Building 2: ", end=" ")
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Not Similar'
unittest.output_test(returned_value, "Not Similar")
print()

print("==============Test Case 3=============")
building_1 = createList(np.array(["Red", "Green", "Yellow", "Red", "Blue", "Green"]))
building_2 = createList(
    np.array(["Red", "Green", "Yellow", "Red", "Blue", "Green", "Blue"])
)
print("Building 1: ", end=" ")
printLinkedList(building_1)
print("Building 2: ", end=" ")
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Not Similar'
unittest.output_test(returned_value, "Not Similar")
print()

print("==============Test Case 4=============")
building_1 = createList(
    np.array(["Red", "Green", "Yellow", "Red", "Blue", "Green", "Blue"])
)
building_2 = createList(np.array(["Red", "Green", "Yellow", "Red", "Blue", "Green"]))
print("Building 1: ", end=" ")
printLinkedList(building_1)
print("Building 2: ", end=" ")
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value)  # This should print 'Not Similar'
unittest.output_test(returned_value, "Not Similar")
print()
