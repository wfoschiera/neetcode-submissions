from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stacks = defaultdict(list)

    def push(self, val: int) -> None:
        cnt = self.count.get(val, 0) + 1
        self.count[val] = cnt
        self.max_count = max(self.max_count, cnt)
        self.stacks[cnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max_count].pop()
        self.count[res] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()