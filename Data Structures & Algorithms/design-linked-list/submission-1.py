class MyLinkedList:

    def __init__(self):
        self._nodes = []

    def get(self, index: int) -> int:
        try:
            return self._nodes[index]
        except IndexError:
            return -1

    def addAtHead(self, val: int) -> None:
        self._nodes = [val] + self._nodes

    def addAtTail(self, val: int) -> None:
        self._nodes.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self._nodes):
            self._nodes = self._nodes[:index] + [val] + self._nodes[index:]

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self._nodes):
            self._nodes = self._nodes[:index] + self._nodes[index+1:]
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)