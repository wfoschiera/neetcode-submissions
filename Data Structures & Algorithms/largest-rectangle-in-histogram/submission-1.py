class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        
        max_h = float("-inf")
        for i, h in enumerate(heights):
            l = r = i
            while True:
                height = heights[i]
                area = height * (r - l + 1)
                # print(f"{i=} {l=} {r=} {height=} {area=}")
                max_area = max(max_area, area)
                if l > 0 and heights[i] <= heights[l - 1]:
                    l -= 1
                elif r < len(heights) - 1 and heights[i] <= heights[r + 1]:
                    r += 1
                else:
                    break

        return max_area