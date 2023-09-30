class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        #Ideas
        # iterate from the right
        # create a stack and it should be monotonic increasing
        # count the number of items in the stack and set that to see
        # if non empty, then add 1 to the items seen

        result = [0] * len(heights)
        stack = []
        
        for i in range(len(heights) - 1, - 1, - 1):
            while stack and stack[-1] < heights[i]:
                result[i] += 1
                stack.pop()
            if stack:
                result[i] += 1
            stack.append(heights[i])

        return result
