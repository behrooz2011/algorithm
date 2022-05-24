arrB =[]
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.arr = []
   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      arrB.append(self.data)
    #   self.arr.append(self.data)
    #   print(" array : ",self.arr)
      if self.right:
         self.right.PrintTree()

# Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()

def auto(x):
    # root = Node
    for i in range(1,x+1):
        if i == 1:
            root = Node(i*100)
        else:
            root.insert(i)
    root.PrintTree()
    print("arrB: ",arrB)
auto(7)