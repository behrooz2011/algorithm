"""257. Binary Tree Paths
Easy
5K
216
Companies
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children."""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Finale:
    solu = []
    def pathF(self,curr, parent):
        # print("pathF")
        stk = []
        res = []
        while (curr):# a node (eventually a leaf)
            stk.append(curr)
            curr = parent[curr] # when curr is None, while breaks
        while len(stk) != 0:
            curr = stk.pop()
            res.append(curr.data)
        return res
    def javab(self,root):#parent maker! very much like preorder traversal
        # print("javab")
        if not root:
           return
       
        nodeStack = []
        nodeStack.append(root)
        parent = {}
        parent[root] = None

        # parentVal ={}
        # parentVal[root.data] = None
       
       
        while len(nodeStack) != 0:
            current = nodeStack.pop()
            # print("cur.data",current.data)
            if (not (current.left) and not (current.right)):
                self.solu.append(self.pathF(current, parent))
            if (current.right):
                parent[current.right] = current
                nodeStack.append(current.right)

                # parentVal[current.right.data] = current.data

            if (current.left):
                parent[current.left] = current
                nodeStack.append(current.left)

                # parentVal[current.left.data] = current.data
    
        # print("parentVal:",parentVal)
        return (self.solu)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(Finale().javab(root))