class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        total = 0
        l = 0
        r = 1
        while r < len(h) -1 and l < r:
            if h[r] >= h[l]:
                hs = [min(h[l], h[r]) - i for i in h[l+1: r]]
                print("hs: ", hs)
                total += sum(hs)
                l = r
                r += 1
            elif h[r] < h[l]:
                r += 1
                continue
        return total
            