
                                                                                                           
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

# 1st check if the root is similar and then the subtrees (basecase)
        if not p and not q:
            return True
        if not p or not q or p.val != q.val: 
            return False

        return(self.isSameTree(p.left,q.left) and 
                self.isSameTree(p.right,q.right))

                    