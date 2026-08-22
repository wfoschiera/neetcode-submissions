class ListNode:
    def __init__(
        self,
        val: int | None = None,
        key: int | None = None,
        next: "ListNode" | None = None,
        prev: "ListNode" | None = None,
    ):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict = {}
        self.head = ListNode()
        self.tail = ListNode(prev=self.head)
        self.head.next = self.tail

    def remove_node_pointers(self, node: ListNode):
        # remove old pointers 
        prev = node.prev
        _next = node.next
        _next.prev = prev
        prev.next = _next

    def update_node(self, node: ListNode):
        # existing node becomes the MRU (most recently used)
        h_next = self.head.next
        node.prev = self.head
        node.next = h_next
        h_next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            self.remove_node_pointers(node)
            self.update_node(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node_pointers(self.cache[key])
        
        self.cache[key] = ListNode(value, key)
        self.update_node(node)

        if len(self.cache) >= self.capacity:
            last_node = self.tail.prev
            self.remove_node_pointers(last_node)
            self.cache.pop(last_node.key)
            

