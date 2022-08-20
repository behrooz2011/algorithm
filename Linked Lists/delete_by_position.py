class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    def delNode(self, head, position):
        if position == 0: # should head be deleted:
            head = head.next
        else:
            temp = head
            count = 1
            while temp != None and count < position:
                temp = temp.next
                count += 1
            temp.next = temp.next.next
        print("this is the head after deletion:",temp.data)

    def lenList(self):
        current = self.head # which is a node
        counter = 0
        while current != None:# as long as this node exists
            counter += 1
            current = current.next
        return counter
LL = LL()
LL.head = Node(3)
print(LL.head.data)#3
LL.head.next = Node(7)
print(LL.head.next.data) #7
LL.head.next.next = Node(4)
print(LL.head.next.next.data)
LL.head.next.next.next = Node(2)
print("length: ",LL.lenList())

LL.delNode(LL.head,1)
print(LL.head.next.data) # this time it must not be 7,but it should be 4
print("new length: ",LL.lenList())