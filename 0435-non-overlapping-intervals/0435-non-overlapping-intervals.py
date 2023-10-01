class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #Idea check if overlap, then remove, and count that removal.
        # Things to remember, [1,2] and [2,3] aren't overlapping

        intervals.sort(reverse = True)

        removals = 0

        res = [intervals[0]]

        for s, e in intervals[1:]:
            if res[-1][0] >= e:
                res.append([s, e])
            else:
                removals += 1

        return removals
        