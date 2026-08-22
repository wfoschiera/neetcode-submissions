# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, target, anc):
            if node is None:
                return
            anc.add(node)
            print(anc)
            if target.val == node.val:
                return 
            elif target.val > node.val:
                return dfs(node.right, target, anc) 
            else:
                return dfs(node.left, target, anc)

        anc_p = set()
        anc_q = set()
        dfs(root, p, anc_p)
        dfs(root, q, anc_q)

        print("final: ", anc_p.intersection(anc_q))

        return root