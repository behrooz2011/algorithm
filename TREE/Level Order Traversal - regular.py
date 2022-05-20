
class Node:
	# A utility function to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# # Iterative Method to print the
# # height of a binary tree


# def printLevelOrder(root):
# 	# Base Case
# 	if root is None:
# 		return

# 	# Create an empty queue
# 	# for level order traversal
# 	queue = []

# 	# Enqueue Root and initialize height
# 	queue.append(root)

# 	while(len(queue) > 0):

# 		# Print front of queue and
# 		# remove it from queue
# 		print(queue[0].data)
# 		node = queue.pop(0)

# 		# Enqueue left child
# 		if node.left is not None:
# 			queue.append(node.left)

# 		# Enqueue right child
# 		if node.right is not None:
# 			queue.append(node.right)





class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.key)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels
# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
j= Solution()

print("Level Order Traversal of binary tree is -")
print(j.levelOrder(root))
# run on terminal:  python "Level Order Traversal - regular.py"