# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        len_l1 = 0
        cur_1 = l1
        while cur_1 is not None:
            len_l1 += 1
            cur_1 = cur_1.next

        len_l2 = 0
        cur_2 = l2
        while cur_2 is not None:
            len_l2 += 1
            cur_2 = cur_2.next

        dummy = ListNode()
        cur = dummy
        next_val = 0
        while l1 is not None or l2 is not None or next_val > 0:
            val1 = val2 = 0
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            if l2 is not None:
                val2 = l2.val
                l2 = l2.next

            val = val1 + val2 + next_val
            next_val = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next
