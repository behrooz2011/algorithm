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
        while (curr):
            stk.append(curr)
            curr = parent[curr]
        while len(stk) != 0:
            curr = stk.pop()
            res.append(curr.data)
            # print(curr.data, end = " ")
        return res
    def javab(self,root):
        # print("javab")
        if not root:
           return
       
        nodeStack = []
        nodeStack.append(root)
        parent = {}
        parent[root] = None
       
       
        while len(nodeStack) != 0:
            current = nodeStack[-1]
            nodeStack.pop(-1)
            # print("cur.data",current.data)
            if (not (current.left) and not (current.right)):
                self.solu.append(self.pathF(current, parent))
            if (current.right):
                parent[current.right] = current
                nodeStack.append(current.right)
            if (current.left):
                parent[current.left] = current
                nodeStack.append(current.left)
        # print("soluuuu: ",self.solu)
        return (self.solu)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(Finale().javab(root))

#Solution: [[1, 2, 4], [1, 2, 5], [1, 3, 6], [1, 3, 7]]