# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        len_l1 = 0
        len_l2 = 0

        cur_1 = l1
        cur_2 = l2

        while cur_1 is not None:
            len_l1 += 1
            cur_1 = cur_1.next

        while cur_2 is not None:
            len_l2 += 1
            cur_2 = cur_2.next
        print(len_l1, len_l2)

        dummy = ListNode()
        cur = dummy
        cur_1 = l1
        cur_2 = l2
        next_val = 0

        while len_l1 > 0 or len_l2 > 0 or next_val > 0:
            print(len_l1, len_l2)
            if len_l1 == len_l2 and len_l1 > 0:
                val1 = cur_1.val
                val2 = cur_2.val
                len_l1 -= 1
                len_l2 -= 1
                cur_1 = cur_1.next
                cur_2 = cur_2.next
                print("if: ", val1, val2)
            elif len_l1 > len_l2:
                val1 = cur_1.val
                val2 = 0
                len_l1 -= 1
                cur_1 = cur_1.next
                print("elif: ", val1, val2)
            elif len_l1 < len_l2:
                val1 = 0
                val2 = cur_2.val
                len_l2 -= 2
                cur_2 = cur_2.next
                print("else: ", val1, val2)
            else:
                val1 = 0
                val2 = 0
            val = val1 + val2 + next_val
            next_val = val // 10
            val = val % 10
            print(f"end. {val=}, {next_val=} ")
            cur.next = ListNode(val)
            cur = cur.next
                
        return dummy.next 