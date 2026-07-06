
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

        if root is None:
            return False
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        