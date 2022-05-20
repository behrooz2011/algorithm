# Python program find maximum element without recursion 


INT_MAX = float('inf')
INT_MIN = - INT_MAX

# A Tree node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to print a maximum and minimum element
# in a tree without recursion without stack
def printMinMax(root,res=[]):
    if root is None:
        print("Tree is empty")
        return
    stack=[]
    stack.append(root)
    print(stack[0].key)
    while stack:
        node = stack.pop()
        res.append(node.key)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        
    print("Max value is :", max(res))

# Driver Code
if __name__ == "__main__":

    # /* 15
    # / \
    # 19 11
    #     / \
    # 25 5
    # / \ / \
    # 17 3 23 24

    # Let us create Binary Tree as shown
    # above */

    root = Node(15)
    root.left = Node(19)
    root.right = Node(11)

    root.right.left = Node(25)
    root.right.right = Node(5)

    root.right.left.left = Node(17)
    root.right.left.right = Node(3)
    root.right.right.left = Node(23)
    root.right.right.right = Node(24)

    # Function call for printing a max
    # and min element in a tree
    printMinMax(root)

