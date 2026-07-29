# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        if root is None:
            return []
        queue.append(root)

        right_most = []
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if i == size - 1:
                    right_most.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return right_most