class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i, text in enumerate(strs):
            ans += text
            if i < len(strs) - 1:
                ans += ":"
        return ans

    def decode(self, s: str) -> List[str]:
        return s.split(":")