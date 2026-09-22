class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        self.helper(1, [], combs, n, k)
        return combs

    def helper(self, i, curComb, combs, n, k):
        if len(curComb) == k:
            combs.append(curComb.copy())
            return 

        if i > n:
            return
        
        # branch 1: include next value
        curComb.append(i)
        self.helper(i + 1, curComb, combs, n, k)
        curComb.pop()


        # branch 2: doesn't include
        self.helper(i + 1, curComb, combs, n, k)
        