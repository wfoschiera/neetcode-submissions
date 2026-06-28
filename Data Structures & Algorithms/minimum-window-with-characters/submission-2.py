from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we iterate over every char in s using the R pointer
        # keeping a hash map to compare against count_t (the goal string)
        # if a char is in count_t and with same qty, we add to have += 1
        # when we get the equality "need == have", we start subtracing the
        # result string, this time, using the L pointer.
        # we will subtract until have == need. So, this way, 
        # we get the shortest string possible
        if t == "":
            return ""

        count_t = Counter(t)
        l = 0
        window = {}

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # if exists and same quantity
            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        # no substring matches
        if res_len == float("infinity"):
            return ""
            
        return s[l : r + 1]