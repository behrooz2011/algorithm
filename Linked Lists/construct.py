#Let's build a LL
class Node:
    def __init__(self):
        self.data = None
        self.next = None
    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next != None
    def listLen(self):
        # print("self.data: ",self.data)
        current = self.data #or head?
        # print("Node:",Node())
        # print("Node.data:",Node().getData())
        count = 0

        while current != None:
            count += 1
            current = self.next
        return count



#Let's create this LL:
# 15 --> 7 --> 40-->Null

ll = Node()
ll.setData(15)
ll.setNext(7)
print(ll.listLen())
