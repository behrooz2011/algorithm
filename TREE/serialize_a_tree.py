""" Convert a tree into a string"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
class Solution:
    def serialize(self,root):
        if not root:
            return ""
        q = []
        q.append(root)
        result = []

        while q:
            node = q.pop(0)
            if node:
                result.append(node.data)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)
        # while result[-1] == None:
        #     result.pop()
        return result
r = Node(1)
r.left = Node(2)
r.right = Node(3)
print(Solution().serialize(r))
""" 123 """  """ <class 'str'>"""

r2 = Node(1)
r2.left = Node(2)
r2.right = Node(3)
r2.right.left = Node(30)
print(Solution().serialize(r2))
