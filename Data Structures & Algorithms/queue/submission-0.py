class Node:
    def __init__(self, value=0, next=None, previous=None):
        self.value= value
        self.next = next
        self.previous = previous

class Deque:
    
    def __init__(self):
        self.start = Node()
        self.end = Node(next=self.start, previous=self.start)
        self.start.next = self.end
        self.start.previous = self.end
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        self.size += 1
        last_node = self.end.previous
        new_node = Node(value=value, previous=last_node, next=self.end)
        self.end.previous = new_node
        last_node.next = new_node

    def appendleft(self, value: int) -> None:
        self.size += 1
        first_node = self.start.next
        new_node = Node(value, previous=self.start, next=first_node)
        self.start.next = new_node
        first_node.previous = new_node        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        last_node = self.end.previous
        previous_node = last_node.previous
        previous_node.next = self.end
        self.end.previous = previous_node
        return last_node.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        first_node = self.start.next
        next_node = first_node.next
        next_node.previous = self.start
        self.start.next = next_node
        return first_node.value
