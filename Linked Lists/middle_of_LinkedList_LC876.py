"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
    def answer(self):
        current = self.head # which is a node
        counter = 0 #length of LL
        while current != None:# as long as this node exists
            counter += 1
            current = current.next
        position = round(counter / 2) if counter % 2 == 1 else round(counter/2)+1
        print("position: ",position)
        newCounter = 1
        temp = self.head
        while temp is not None and newCounter < position:
            newCounter += 1
            temp = temp.next
        return temp.val
LL = Solution()
LL.head = ListNode(4)
LL.head.next = ListNode(5)
L3 = LL.head.next.next = ListNode(70)
LL.head.next.next.next = ListNode(1)

print(LL.answer())