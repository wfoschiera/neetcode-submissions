class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
    
    def get(self, index: int) -> int:
        curr = self.head.next
        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next
        return curr.value if curr is not None else -1

    def insertHead(self, val: int) -> None:
        new_node = Node(value=val)
        first_node = self.head.next
        new_node.next = first_node
        self.head.next = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(value=val)
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = new_node

    def remove(self, index: int) -> bool:
        curr = self.head
        for i in range(index):
            if curr.next is None:
                return False
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        node = self.head.next
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next
        return values
