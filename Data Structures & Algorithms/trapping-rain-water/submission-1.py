class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = 1
        while left <= right and right < len(height)-1:
            print(left, right)
            if height[right] >= height[left]:
                values = [min(height[left], height[right]) - i for i in height[left+1: right]]
                total += sum(values)
                left = right
                right += 1
            elif height[right] <= height[left]:
                right += 1
                continue
        return total
            