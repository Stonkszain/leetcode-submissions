class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)

        # BRUTE FORCE Approach

        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break

        # Stack approach
        # loop through the temperatures
        # each time check if the current temp is greater than the stack ones, if yes then pop stack
        # if not then add to stack. When adding to stack, add value and index pair

        stack = list()

        for idx, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                result[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()
            stack.append((val, idx))
        
        return result


        