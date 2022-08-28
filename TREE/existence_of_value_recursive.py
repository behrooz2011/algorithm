class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
class Solution:
    def existence_preorder(self,root,nodeVal):
        print("started")
        if(root is None):
            # print("false...")
            return 0
        if root.data == nodeVal:
            # print("YES")s
            return 10
        self.existence_preorder(root.left,nodeVal)
        self.existence_preorder(root.right, nodeVal)


""" Main solution is down here"""

class Main:
    def __init__(self):
        self.counter = 1
    def existence_preorder(self,root,nodeVal):
        print("hi",self.counter)
        self.counter += 1
        if root is None:
            return False
        if root.data == nodeVal:
            print("yes......")
            return True

        leftVal = self.existence_preorder(root.left,nodeVal)
        # node found, no need to look further
        # if leftVal == 1:
        #     return True
        rightVal = self.existence_preorder(root.right, nodeVal)
          #node is not found in le so recur on right subtree """
        # if rightVal == 1:
        #     return True
        # return False
        if leftVal or rightVal:
            return True
        else:
            return False



r=Node(1)
r.left= Node(2)
r.right = Node(3)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.left= Node(6)
r.right.right = Node(7)


# sol = Solution()
# print(sol.existence_preorder(r,2))

# print(Main().existence_preorder(r,50))
# print(Main().existence_preorder(r,5))
# print(Main().existence_preorder(r,1))
print(Main().existence_preorder(r,5))