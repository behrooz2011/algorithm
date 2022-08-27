class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
class Solution:
    def pre(self, root, result):
        if root is None:
            return
        stack = [] #Nodes will come here not values
        stack.append(root)

        while stack :
            node = stack.pop()
            result.append(node.data)

            if node.right:
                stack.append(node.right)
            if node.left :
                stack.append(node.left)
        # return max(result)
        return (result)


    def maxValue(self,root):
        if root is None:
            return
        maxVal = float('-inf')
        stack = [] #Nodes will come here not values
        stack.append(root)

        while stack :
            node = stack.pop()
            maxVal = max(maxVal,node.data)
            if node.right:
                stack.append(node.right)
            if node.left :
                stack.append(node.left)
        # return max(result)
        return maxVal
r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(40)
r.left.right = Node(5)
r.right.right = Node(70)
r.right.left= Node(6)

print("ino ",Solution().pre(r,[]))
print("max ",Solution().maxValue(r))