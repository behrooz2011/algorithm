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
        # current = self.data #or head?
        # print("Node:",Node())
        # print("Node.data:",Node().getData())
        # count = 0

        # while current != None:
        #     count += 1
        #     current = self.next
        # return count
        print("self.data: ",self.data)
        current = self
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count
    def getNodeDataByIndex(self, index):
        current = self
        count = 0
        while current is not None:
            if count == index:
                return current.getData()
            count += 1
            current = current.getNext()
        return None  # Return None if the index is out of range



#Let's create this LL:
# 15 --> 7 --> 40-->Null

# ll = Node()
# ll.setData(15)
# ll.setNext(7)
# print(ll.listLen())

# Creating nodes
node1 = Node()
node1.setData(15)

node2 = Node()
node2.setData(7)

node3 = Node()
node3.setData(40)

# Linking nodes
node1.setNext(node2)
node2.setNext(node3)

# Now the list is: 15 --> 7 --> 40 --> Null
print(node1.listLen())  # Output should be 3
third_node_data = node1.getNodeDataByIndex(3)
print(third_node_data) 