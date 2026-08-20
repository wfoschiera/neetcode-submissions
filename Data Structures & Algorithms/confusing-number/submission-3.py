class Solution:
    def confusingNumber(self, n: int) -> bool:
        inv_map = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        inverted = ""
        for num in str(n):
            if num not in inv_map:
                return False
            inverted = inv_map[num] + inverted
        return int(inverted) != n