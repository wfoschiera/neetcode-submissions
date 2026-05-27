class StepNode:

    def __init__(self, url=None, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev =prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = StepNode(homepage)

    def visit(self, url: str) -> None:
        visited = StepNode(url, next=None, prev=self.curr)
        self.curr.next = visited
        self.curr = visited

    def back(self, steps: int) -> str:
        cur = self.curr
        for i in range(steps):
            if cur.prev == None:
                break
            cur = cur.prev

        self.curr = cur
        return cur.url

    def forward(self, steps: int) -> str:
        cur = self.curr
        for i in range(steps):
            if cur.next == None:
                break
            cur = cur.next

        self.curr = cur
        return cur.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
