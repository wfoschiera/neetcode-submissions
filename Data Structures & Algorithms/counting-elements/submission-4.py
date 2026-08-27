class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        visited = set()
        count = 0
        for i in range(0, len(arr)):
            if arr[i]+1 in arr_set:
                visited.add(arr[i])
                count += 1

        return count

