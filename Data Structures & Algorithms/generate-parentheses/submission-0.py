class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(b_open: int, b_close: int, cur_comb: str):
            if len(cur_comb) == 2 * n and b_close == b_open:
                res.append(cur_comb)

            if b_close > b_open or b_open > n:
                return

            helper(b_open+1, b_close, cur_comb+"(")
            helper(b_open, b_close+1, cur_comb+")")

        helper(0, 0, "")

        return res