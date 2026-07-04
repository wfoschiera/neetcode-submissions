class MyHashSet: 
    """
    Brute force Solution (Without builtin set)
    """
    def __init__(self):
        self._items = []

    def add(self, key: int) -> None:
        if key not in self._items:
            self._items.append(key)

    def remove(self, key: int) -> None:
        if key in self._items:
            self._items.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._items


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)