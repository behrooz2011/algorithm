"""102. Binary Tree Level Order Traversal
Medium
11.3K
214
Companies
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 """
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
def levelOrder(root):
    if root is None:
        return
    res = []
    level = []
    k = 0
    stack = []
    stack.append([root,0])
    # print("stack",stack)
    while stack:
        node = stack.pop(0)
        # if len(level) == 0:
        #     level.append(node[0].val)
        if node[1] == k:
            level.append(node[0].data)
        else:
            res.append(level)
            level = []
            level.append(node[0].data)
            k += 1
        # res.append(node[0].data)

        if node[0].left:
            stack.append([node[0].left, node[1]+1])
        if node[0].right:
            stack.append([node[0].right, node[1]+1])
    res.append(level) #for the last level that is left behind bcz of the else statement
    # print("k",k)
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(levelOrder(root))
"[[1], [2, 3], [4, 5, 6, 7]]"