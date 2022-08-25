"Level Order Traversal with empty nodes included"
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right =None
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
            levels[level].append(node.data)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            else:
                if(level + 1 < len(levels)):
                    levels[level+1].append("null")
            if node.right:
                helper(node.right, level + 1)
            else:
                if(level + 1 < len(levels)):
                    levels[level+1].append("null")
            # else:
            #     levels[level].append("null")
            
        helper(root, 0)
        return levels
r = Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.right = Node(100)
r.left.right.right=Node(40)
print(Solution().levelOrder(r))
""" 
                    1
                   / \
                  /   \
                 2     3
                / \     \
               /   \     \
              4     5     100
                     \
                      \
                       40
                        
"""
" result = [[1], [2, 3], [4, 5, 'null', 100], [40, 'null', 'null']] "