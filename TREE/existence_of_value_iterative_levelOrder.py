#LEVEL Traversal 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right= None
class Solution:
    def levelOrder(self,root, result):
        if root is None:
            return 
        queue = [] 
        queue.append(root)
        result.append(root.data)

        while queue:
            node = queue.pop()
            if node.left:
                result.append(node.left.data)
                queue.insert(0,node.left)
            if node.right:
                result.append(node.right.data)
                queue.insert(0,node.right)
        return result


r=Node(1)
r.left= Node(2)
r.right = Node(3)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.left= Node(6)
r.right.right = Node(7)

print(Solution().levelOrder(r,[]))