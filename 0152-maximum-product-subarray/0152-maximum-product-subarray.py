import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # O(n^2)
        # max_prod = -sys.maxsize

        # for i in range(len(nums)):
        #     cur_prod = 1
        #     for j in range(i, len(nums)):
        #         cur_prod *= nums[j]
        #         max_prod = max(max_prod, cur_prod)

        # return max_prod

        max_prod = nums[0]
        cur_max, cur_min = 1, 1

        for i in nums:
            tmp = cur_max * i

            cur_max = max(tmp, i * cur_min, i)
            cur_min = min(tmp, i * cur_min, i)

            max_prod = max(cur_max, max_prod)

        
        return max_prod
