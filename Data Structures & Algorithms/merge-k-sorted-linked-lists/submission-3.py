# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or lists == [[]]:
            return 
        l, r = 0, len(lists) - 1
        while l < r:
            node_l = lists[l]
            node_r = lists[r]
            head = self.merge_nodes(node_l, node_r)
            lists[0] = head
            r -= 1
        return lists[0]

    def merge_nodes(self, node_l, node_r):
        dummy = ListNode()
        tail = dummy
        while node_l is not None or node_r is not None:
            if node_l is not None and node_r is None:
                tail.next = node_l
                tail = node_l
                node_l = node_l.next
            elif node_l is None and node_r is not None:
                tail.next = node_r
                tail = node_r
                node_r = node_r.next
            elif node_l.val <= node_r.val:
                tail.next = node_l
                tail = node_l
                node_l = node_l.next
            else:
                tail.next = node_r
                tail = node_r
                node_r = node_r.next
        return dummy.next