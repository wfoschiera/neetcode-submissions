# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from dataclasses import dataclass

@dataclass
class ThreeMetadata:
    is_balanced: bool
    three_height: int
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode) -> ThreeMetadata:
            if node is None:
                return ThreeMetadata(True, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            is_balanced = left.is_balanced and right.is_balanced and abs(left.three_height - right.three_height) <= 1
            
            return ThreeMetadata(is_balanced, 1 + max(left.three_height, right.three_height))

        return dfs(root).is_balanced