'''
LC 141:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''
# Definition for singly-linked list.
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

class Solution:
    def hasCycle(self, head):
        nodes_seen = set()
        while head.head is not None:#head should be a node
            print("head not None")
            if head.head.val in nodes_seen:
                return True
            nodes_seen.add(head.head.val)
            # print("end of if")
            print("head.val ", head.head.val)
            print("SET: ",nodes_seen)
            head.head = head.head.next
        return False
""" [ 3--> 2--> 1--> -4--> 2[similar 2 at pos 1] """
#let's build it
ll =LinkedList()
ll.head = Node(3)
ll.head.next = Node(2)
# print("ll.head.next",ll.head.next.val)
ll.head.next.next = Node(1)
ll.head.next.next.next = Node(-4)
ll.head.next.next.next.next = Node(2)
jj = Solution()
print(jj.hasCycle(ll))


""" Space complexity O(1): two pointer === two racers """
class Solution:
    def hasCycle(self, head) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True