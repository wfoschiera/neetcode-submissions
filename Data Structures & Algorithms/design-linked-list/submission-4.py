class ListNode:
    def __init__(self, val: int = 0, next: None | ListNode = None, prev: None | ListNode = None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if self.size <= index:
            return -1
        cur = self.head.next
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        head = self.head
        new_node.next = head.next
        new_node.prev = head
        head.next = new_node
        new_node.next.prev = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        tail = self.tail
        new_node.next = tail
        new_node.prev = tail.prev
        new_node.prev.next = new_node
        tail.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index == self.size:
            self.addAtTail(val)
            return
        new_node = ListNode(val)
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        new_node.next = cur
        new_node.prev = cur.prev
        new_node.prev.next = new_node
        cur.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index:
            return

        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.size -= 1
        del cur


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
