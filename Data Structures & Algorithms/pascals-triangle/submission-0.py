class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        def get_row(row_above):
            size = len(row_above)
            cur_row = [1] * (size + 1)
            for i in range(len(cur_row)):
                if i == 0 or i == len(cur_row) - 1:
                    continue
                cur_row[i] = row_above[i] + row_above[i-1]
            return cur_row

        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                row_above = res[-1]
                res.append(get_row(row_above))
        return res