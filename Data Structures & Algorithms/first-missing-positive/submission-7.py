class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Brute force solution
        # O(n) time
        # O(n) extra space
        # seen = set()
        # highest_not_seen = 1
        # for num in nums:
        #     seen.add(num)
        # while highest_not_seen in seen:
        #     highest_not_seen += 1

        # return highest_not_seen

        ### OPTIMAL SOLUTION ###
        # O(n) time
        # O(1) extra space
        # solution set (conjunto solução) is between [1, len(nums) + 1]

        # default value to set when that index is already 0 (masked)
        upper_bound = len(nums) + 1
        # first, create a mask removing every negative value
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            # since the input array is masked, whe will check
            # for values and map them to its index
            val = abs(nums[i])

            # for every num in input array, we will mark if the number exists
            # using the number idx, since our solution set allow to this.
            if 1 <= val <= len(nums):
                num_at_idx = nums[val - 1]
                # if the number is positive, set as negative
                if num_at_idx > 0:
                    nums[val - 1] *= -1
                # if the number was previously masked, set as the default negative (out o solution set)
                elif num_at_idx == 0:
                    nums[val - 1] = -upper_bound

        # in this last loop, check each number in the array >=0. 
        # since we use the array position to mark if the number exists
        # and set this number as negative, the first to be >=0 at number position
        # is the missing one. If any is missing, then the highest positive integer is
        # the len(array) + 1.
        for i in range(1, upper_bound):
            if nums[i - 1] >= 0:
                return i
        return upper_bound