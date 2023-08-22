import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #bruteforce approach
        
        # max_sum = -sys.maxsize
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums) + 1):
        #         subarray_sum = 0
        #         for k in nums[i:j]:
        #             subarray_sum += k
        #         if subarray_sum > max_sum:
        #             max_sum = subarray_sum
                
        # return max_sum

        # quadratic method
        # max_sum = -sys.maxsize

        # for i in range(len(nums)):
        #     subarray_sum = 0
        #     for j in range(i, len(nums)):
        #         subarray_sum += nums[j]
        #         if subarray_sum > max_sum:
        #             max_sum = subarray_sum
        # return max_sum

        # O(n) method
        
        max_sum = nums[0]
        cur_sum = 0

        for i in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            max_sum = max(max_sum, cur_sum)

        return max_sum
