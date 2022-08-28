''' 
                    1
                   / \
                  2   3
                 / \ / \
                4  5 6  7

output =[4, 5, 6, 7, 2, 3, 1]

'''
class Node:
    def __init__(self,data):
        self.data  = data
        self.left = self.right = None
class Solution:
    def reverse(self,root,result):
        if root is None:
            return
        q = []
        q.append(root)
        result.insert(0,root.data)
        
        while q:
            root = q.pop()
            if root.right:
                q.insert(0,root.right)
                result.insert(0,root.right.data)
            if root.left:
                q.insert(0,root.left)
                result.insert(0,root.left.data)
        return result
r=Node(1)
r.left= Node(2)
r.right = Node(3)

r.left.left=Node(4)
r.left.right = Node(5)
r.right.left= Node(6)
r.right.right = Node(7)

print("Reverse:",Solution().reverse(r,[]))
