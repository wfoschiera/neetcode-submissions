class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        val = 0
        for i in range(len(stones)):
            val = abs(val - stones[i])
            print(i, val)
        return val