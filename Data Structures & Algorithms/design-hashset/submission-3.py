# class MyHashSet: 
#     """
#     Brute force Solution (Without builtin set)
#     """
#     def __init__(self):
#         self._items = []

#     def add(self, key: int) -> None:
#         if key not in self._items:
#             self._items.append(key)

#     def remove(self, key: int) -> None:
#         if key in self._items:
#             self._items.remove(key)

#     def contains(self, key: int) -> bool:
#         return key in self._items

class MyHashSet: 
    """
    Optimal Solution (trying to reproduce after seeing it)
    This solution will use 31250 integers with 32 bits each 
    """
    def __init__(self):
        # 0 < 1_000_000
        # 1_000_000 / 32 bits = 31250  
        self._items = [0] * 31250

    def add(self, key: int) -> None:
        # split the key in 32 parts
        # to find the integer. Each integer
        # has 32 bit size. Each bit related
        # to a specific value
        # | OR set bit to 1 
        self._items[key // 32] |= self.get_mask(key)

    def remove(self, key: int) -> None:
        # first we need to get the right integer
        # then, flip the bit on the position
        # ^= XOR set bit to 1 if bit is different
        if self.contains(key):
            self._items[key // 32] ^= self.get_mask(key)

    def contains(self, key: int) -> bool:
        # & Sets bit to 1 if both bits are 1
        return self._items[key // 32] & self.get_mask(key) != 0
    
    def get_mask(self, key: int):
        return 1 << (key % 32) 