class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(open_p: int, close_p: int, cur_comb: str):
            # if len(cur_comb) == 2 * n
            # using this condition we make sure that cases like "(("
            # for n=2 will not be possible
            if close_p == open_p == n:
                res.append(cur_comb)

            if close_p > open_p or open_p > n:
                return

            # optimization:
            # avoid to explore branches when open_p > n
            # or close_p > open_p
            if open_p < n:
                helper(open_p+1, close_p, cur_comb+"(")
            if close_p < open_p:
                helper(open_p, close_p+1, cur_comb+")")

        helper(0, 0, "")

        return res