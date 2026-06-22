class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force without hints
        # res = []

        # for i, temperature in enumerate(temperatures):
        #     count = 1
        #     has_warmth = False
        #     for next_temp in temperatures[i + 1 :]:
        #         if next_temp > temperature:
        #             has_warmth = True
        #             res.append(count)
        #             break
        #         count += 1

        #     if not has_warmth:
        #         res.append(0)
        # return res

        res = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_ind = stack.pop()
                res[stack_ind] = i - stack_ind

            stack.append((temp, i))
        return res
