class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            # if left side is sorted
            if nums[l] <= nums[mid]:
                # if target is in the sorted side
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            # if right side is sorted
            elif nums[r] > nums[mid]:
                # if target is in the sorted side
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
