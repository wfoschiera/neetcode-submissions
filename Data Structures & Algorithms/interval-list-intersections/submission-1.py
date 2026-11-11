class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            start_i, end_i = firstList[i]
            start_j, end_j = secondList[j]
            
            if start_i <= start_j <= end_i:
                res.append([max(start_j, start_i), min(end_i, end_j)])
                
            elif start_j <= start_i <= end_j:
                res.append([max(start_j, start_i), min(end_i, end_j)])

            if end_i > end_j:
                j += 1
            else:
                i += 1

        return res