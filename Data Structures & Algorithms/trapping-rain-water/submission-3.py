class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Verbose solution
        """
        if not height:
            return 0

        h = height
        l, r = 0, len(h) - 1
        left_max, right_max = h[l], h[r]
        total = 0

        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, h[l])
                w = min(left_max, right_max) - h[l]
                total += max(w, 0)
                
            else:
                r -= 1
                right_max = max(right_max, h[r])
                w = min(left_max, right_max) - h[r]
                total += max(w, 0)
        return total
            