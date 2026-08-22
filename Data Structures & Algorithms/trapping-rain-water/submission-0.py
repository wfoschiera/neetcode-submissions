class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = 1
        while left <= right and right < len(height)-1:
            print(left, right)
            if height[right] >= height[left]:
                left = right
                right += 1
                print("Sum: ", height[left: right])
                print("Left: ", left, "Right: ", right)
                total += sum(height[left:right])
            elif height[right] <= height[left]:
                
                
                right += 1
                continue
            
            
        return total
            