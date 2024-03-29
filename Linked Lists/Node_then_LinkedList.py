### first define the Node class and then give it to a LL class 



# class Node:
#   # constructor
#   def __init__(self, data, next=None): 
#     self.data = data
#     self.next = next

# # Creating a single node
# first = Node(3)
# print(first.data)
# print(first.next)

# second = first.next = Node(10)
# print(first.data)
# print(second.data)
# print("first next",first.next.data)

# third = second.next = Node(7)
# print(third.data)
# print(third.next)




#############################################################
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):  
        self.head = None
    def lenList(self):
        current = self.head # which is a node
        counter = 0
        while current != None:# as long as this node exists
            counter += 1
            current = current.next
        return counter

""" Make a LL from an array"""      
def makeFromArray(arr):
    print("create a linked list from an array")
    res = LinkedList()
    res.head = Node(arr[0])
    temp = res.head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return res

makeFromArray([7 ,9 , 12, 1 , 0 , 100, -7])
result = makeFromArray([7 ,9 , 12, 1 , 0 , 100,-7])
print("length of this new LL: ",result.lenList())


# Linked List with a single node
LL = LinkedList()
LL.head = Node(3)
print(LL.head.data)#3
LL.head.next = Node(7)
print(LL.head.next.data) #7
LL.head.next.next = Node(4)
print(LL.head.next.next.data)
print("len",LL.lenList())

