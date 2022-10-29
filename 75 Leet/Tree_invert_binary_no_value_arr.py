"""226. Invert Binary Tree
Easy
10.1K
142
Companies
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        temp=root
        # result=[]
        stack = []
        stack.append(root)
        # print(root.left.left)
        # print("root: ",root)
        while stack:
            root = stack.pop(0)
            # result.append(root.val)
            left = root.left
            right = root.right

            root.left=right
            root.right=left
            
            if root.right:stack.append(root.right)
            if root.left:stack.append(root.left)
            
        # print(result)
        return temp