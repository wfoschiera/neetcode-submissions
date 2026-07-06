# class Solution:
#     def trap(self, height: List[int]) -> int:
#         """
#         Verbose solution
#         """
#         if not height:
#             return 0

#         h = height
#         l, r = 0, len(h) - 1
#         left_max, right_max = h[l], h[r]
#         total = 0

#         while l < r:
#             if left_max <= right_max:
#                 l += 1
#                 left_max = max(left_max, h[l])
#                 w = min(left_max, right_max) - h[l]
#                 total += max(w, 0)
                
#             else:
#                 r -= 1
#                 right_max = max(right_max, h[r])
#                 w = min(left_max, right_max) - h[r]
#                 total += max(w, 0)
#         return total
            
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Simplified version
        added comments to better understand WHY it could be simplified
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
                # since we update left_max before calculate trapped water
                # and we know that left_max < right_max
                # left_max - h[l] will always be positive or 0 (subtract itself)
                left_max = max(left_max, h[l])
                total += left_max - h[l]
            else:
                r -= 1
                right_max = max(right_max, h[r])
                total += right_max - h[r]
        return total
            