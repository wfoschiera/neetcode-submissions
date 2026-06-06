class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        max_cont = 0
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            
            cont = 1
            while num + cont in set_nums:
                cont += 1   
            if cont > max_cont:
                max_cont = cont

        return max_cont
