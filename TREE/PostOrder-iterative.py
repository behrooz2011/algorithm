class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
def postIterative(root,result):
    if not root:
        return
    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else: #leaf case
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None
    return result
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(postIterative(root,result=[]))
#[4, 5, 2, 6, 7, 3, 1]