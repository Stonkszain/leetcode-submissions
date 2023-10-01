class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Idea if intervals overlap, then merge, if not then don't merge

        intervals.sort(key = lambda i : i[0])

        result = []

        for i in range(len(intervals)):
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(intervals[i][1], result[-1][1])

        return result
