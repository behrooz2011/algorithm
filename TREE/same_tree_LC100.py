class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def isSameTree(self, p, q):
        print("preQ: ",self.preQ(q,[]))
        print("preP: ",self.preP(p,[]))
        return (self.preQ(q,[]) == self.preP(p,[]))
        
    def preQ(self,q,result=[]):
        if q is None:
            result.append('null') #this is necessary otherwise, [1,2] and [1,null,2] will produce True
            return
        result.append(q.val)
        self.preQ(q.left,result)
        self.preQ(q.right,result)
        return result
        
    def preP(self,p,result=[]):
        if p is None:
            result.append('null')
            return
        result.append(p.val)
        self.preP(p.left,result)
        self.preP(p.right,result)
        return result
""" Shorter Solution"""
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)