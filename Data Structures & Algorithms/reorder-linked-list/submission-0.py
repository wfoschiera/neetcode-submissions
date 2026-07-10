# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def order_list(values):
            mid = len(values) // 2
            l1 = values[:mid]
            l2 = values[mid:]
            l2 = l2[::-1]
            ordered_list = []
            for i, j in zip(l1, l2):
                ordered_list += [i, j]
            if len(values) % 2 == 1:
                ordered_list.append(l2[-1])
            return ordered_list

        cur = head
        values = []
        while cur is not None:
            values.append(cur.val)
            cur = cur.next

        ordered_values = order_list(values)
        print("ordered: ", ordered_values)
        nodes = []
        for val in ordered_values:
            nodes.append(ListNode(val))

        cur = head
        for idx in range(len(nodes)):
            if idx + 1 < len(nodes):
                cur.next = nodes[idx + 1]
                cur = cur.next

        return