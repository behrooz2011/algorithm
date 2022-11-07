class Node:
    def __init__(self,data):
        self.data = data
        self.left =self.right = None
class Solution:
    def isSubtree(self, s,t):
        if not t: return True # if the smaller tree,t  is null then it's definitely a subtree of the bigger tree S
        if not s: return False
        
        if self.sameTree(s,t):
            return True
        else:
            return(self.isSubtree(s.left, t) or
            self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.data == t.data:
            return(self.sameTree(s.left,t.left) and 
            self.sameTree(s.right, t.right))
        return False
        


""" Sub-Optimal approach """
class Solution(object):

    def preP(self,p,result=[]):
        if p is None:
            result.append('null')
            return
        result.append(p.val)
        self.preP(p.left,result)
        self.preP(p.right,result)
        return result
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        print("result: ",self.preP(root,[])) # sublist formula down below
        return (self.preP(subRoot,[]) in [self.preP(root,[])[i:len(self.preP(subRoot,[]))+i] for i in range(len(self.preP(root,[])))])

        """ Sublist formula:
        a = [2,4,3,5,7]
        b = [2,4]
        print(b in [a[i:len(b)+i] for i in range(len(a))]) ==>True"""