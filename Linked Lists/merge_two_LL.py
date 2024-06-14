"""21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Initialize a dummy node to act as the start of the merged list
    dummy = ListNode()
    current = dummy

    # Traverse both lists and append the smaller value to the merged list
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If any elements are left in either list, append them to the merged list
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    # The merged list is next to the dummy node
    return dummy.next

# Helper function to convert a list to a linked list
def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Examples
list1 = to_linked_list([1, 2, 4])
list2 = to_linked_list([1, 3, 4])
merged_list = mergeTwoLists(list1, list2)
print(to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]

list1 = to_linked_list([])
list2 = to_linked_list([])
merged_list = mergeTwoLists(list1, list2)
print(to_list(merged_list))  # Output: []

list1 = to_linked_list([])
list2 = to_linked_list([0])
merged_list = mergeTwoLists(list1, list2)
print(to_list(merged_list))  # Output: [0]
