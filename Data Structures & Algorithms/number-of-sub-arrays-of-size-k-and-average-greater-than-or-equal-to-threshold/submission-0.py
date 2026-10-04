from collections import deque


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarray = deque()
        count = 0

        for num in arr:
            if len(subarray) >= k:
                subarray.popleft()
            subarray.append(num)

            if len(subarray) < k:
                continue

            if sum(subarray) / k >= threshold:
                count += 1
        return count
