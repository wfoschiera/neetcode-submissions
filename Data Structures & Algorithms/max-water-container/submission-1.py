class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water_max = 0
        l = 0
        r = len(heights) - 1
        len_h = len(heights)
        for l in range(len_h):
            for r in range(len_h-1, 0, -1):
                max_h = min(heights[l], heights[r]) * (r - l)
                water_max = max(max_h, water_max)
        
        return water_max
