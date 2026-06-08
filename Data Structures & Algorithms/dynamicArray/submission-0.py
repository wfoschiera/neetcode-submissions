class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self._array = [None] * self.capacity

    def get(self, i: int) -> int:
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self._array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self._array[self.size]

    def resize(self) -> None:
        self._array = self._array + [None] * self.capacity
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
