class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        # self.q2.append(x)
        # while self.q1:
        #     self.q2.append(self.q1.popleft())

        # self.q1, self.q2 = self.q2, self.q1
        self.q1.appendleft(x)

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return bool(not self.q1)