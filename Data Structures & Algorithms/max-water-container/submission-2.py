class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water_max = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            max_h = min(heights[l], heights[r]) * (r - l)
            water_max = max(max_h, water_max)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return water_max
