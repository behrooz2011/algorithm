""" Previously

LL = LinkedList()
LL.head = Node(3)
LL.head.next = Node(7)
LL.head.next.next = Node(4)

One head, all next
"""
class ListNode:
   def __init__(self, data, next = None):
      self.data = data
      self.next = next
class List:#linked list
    def __init__(self):  
        self.head = None

""" Internet Solution"""
# def make_list(elements):#gets the lists of elements
#    head = ListNode(elements[0]) # Make the head
#    for element in elements[1:]: # from the second element forward
#       ptr = head
#       while ptr.next:
#          ptr = ptr.next
#          ptr.next = ListNode(element)
#    return head

"""
My solution
"""
def makeFromArray(arr):
    print("create a linked list from an array")
    res = LinkedList()
    res.head = Node(arr[0])
    temp = res.head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return res

"""
It should be sth like this:
List().head = Node( elem 1)
List().head.next = Node( elem 2)
List().head.next.next = Node( elem 3)
....

"""