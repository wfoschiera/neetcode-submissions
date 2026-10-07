class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = cnt = 0
        sign = "="

        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                cnt = cnt + 1 if sign == "<" else 1
                sign = ">"
            elif arr[i] < arr[i+1]:
                cnt = cnt + 1 if sign == ">" else 1
                sign = "<"
            else:
                cnt = 0
                sign = "="

            res = max(res, cnt)
        
        return res + 1
            