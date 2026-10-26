# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = float("-inf")
        stack = []
        node = head


        while node:
            stack.append(node)
            node = node.next

        j = (len(stack) // 2)
        i = j -1

        while i >= 0 and j < len(stack):
            sum_i_j = stack[i].val + stack[j].val
            max_sum = max(max_sum, sum_i_j)
            i -=1
            j += 1

        return max_sum
