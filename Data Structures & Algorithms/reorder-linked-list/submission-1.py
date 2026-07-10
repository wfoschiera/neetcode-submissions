# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #     """Brute force solution.
        #     Mistakes I've made here:
        #     - split in two parts and reordering the second part (could link the nodes in inverse order)
        #     - create a list of values instead a list of nodes (more rich objects)
        #     - recreating the entire list of nodes from de value
        #     """
        #     def order_list(values):
        #         """this is not even close of the best way to do"""
        #         mid = len(values) // 2
        #         l1 = values[:mid]
        #         l2 = values[mid:]
        #         l2 = l2[::-1]
        #         ordered_list = []
        #         for i, j in zip(l1, l2):
        #             ordered_list += [i, j]
        #         if len(values) % 2 == 1:
        #             ordered_list.append(l2[-1])
        #         return ordered_list

        #     cur = head
        #     values = []
        #     while cur is not None:
        #         values.append(cur.val)
        #         cur = cur.next

        #     ordered_values = order_list(values)
        #     print("ordered: ", ordered_values)
        #     nodes = []
        #     for val in ordered_values:
        #         nodes.append(ListNode(val))

        #     cur = head
        #     for idx in range(len(nodes)):
        #         if idx + 1 < len(nodes):
        #             cur.next = nodes[idx + 1]
        #             cur = cur.next

        #     return

        """SECOND TRY. Let's adress some of the previous mistakes"""

        # FIRST: create a list of nodes. In brute force solution it
        # allows to use two pointers
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next

        # two pointers approach
        i, j = 0, len(nodes) - 1
        while i < j:
            # link the first node to the last one
            nodes[i].next = nodes[j]
            i += 1
            # if iteration over first nodes over, break the loop
            if i >= j:
                break
            # link the last node to the second (i+1 was done before)
            nodes[j].next = nodes[i]
            j -= 1
        # clear the last node (first part last node) next
        nodes[i].next = None
