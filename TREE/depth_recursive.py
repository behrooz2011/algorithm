# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))


#lets build the tree with the following input:
#input : [3,9,20,null,null,15,7]  to be deployed in level-order traversal
# how to create a tree with an array
# Expected output: 3


        