# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head 
        
        prev = None
        cur = head
        for i in range(k):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        tail = head
        tail.next = self.reverseKGroup(cur, k)
        return prev
        
