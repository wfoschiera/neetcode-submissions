class MyHashMap:

    def __init__(self):
        self._keys = []
        self._values = []

    def put(self, key: int, value: int) -> None:
        self.upsert(key, value)

    def get(self, key: int) -> int:
        if key not in self._keys:
            return -1
        idx = self._keys.index(key)
        return self._values[idx]
        

    def remove(self, key: int) -> None:
        if key not in self._keys:
            return
        idx = self._keys.index(key)
        self._keys.pop(idx)
        self._values.pop(idx)
        
    def upsert(self, key:int, value: int) -> None:
        if key in self._keys:
            idx = self._keys.index(key)
            self._values[idx] = value
        else:
            self._keys.append(key)
            self._values.append(value)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)