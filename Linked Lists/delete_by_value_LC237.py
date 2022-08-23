'''
Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, instead you will be given access to the node 
to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.
'''
# Definition for singly-linked list.
# from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head =  None
    def deleteNode(self, node):#leetcode answer
        # node = ListNode(node)
        print("Node: ",node)
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return
    "Give the length of the Linked List"
    def lenList(self):
        current = self.head # which is a node
        counter = 0
        while current != None:# as long as this node exists
            counter += 1
            current = current.next
        return counter
    "Give an array of node values"
    def giveList(self):
        arr =[]
        current = self.head
        # print("self.head",self.head)
        while current != None:
            arr.append(current.val)
            current = current.next
        return arr

    def myDelApproach(self,data):
        print("head val:",self.head)
        if self.head.val == data:
            print("Head to be removed...")
            self.head = self.head.next
            return
        else:
            current = self.head
            while current.val != data:
                current = current.next
            current.val = current.next.val
            current.next = current.next.next
            return



LL = Solution()
LL.head = ListNode(4)
LL.head.next = ListNode(5)
L3 = LL.head.next.next = ListNode(3)
LL.head.next.next.next = ListNode(1)
print("length: ",LL.lenList())
print("length: ",LL.lenList())
print("length: ",LL.lenList())

""" This would change the structure of the Linked List if there were assignments without temp variable"""
print("Array: ",LL.giveList())
print("length: ",LL.lenList())

# LL.deleteNode(L3)#3
# print("\nDelete a node value")
# print("length: ",LL.lenList())
# print("Array: ",LL.giveList())

print("\nDelete a node value")
print("DEL:",LL.myDelApproach(3))
print("length: ",LL.lenList())
print("Array: ",LL.giveList())
print(LL.head.next.next.val) # this time it is not 3, it's 1