# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        steps = 0
        cur = head
        while cur is not None:
            steps += 1
            cur = cur.next
        if steps == 1 and n == 1:
            return 

        cur = head
        step2 = 0
        while cur is not None:
            step2 += 1
            if step2 == (steps - n):
                cur.next = cur.next.next
            cur = cur.next
        return head
