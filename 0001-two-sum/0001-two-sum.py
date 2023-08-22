class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = dict()

        for i in range(len(nums)):
            temp = target - nums[i]
            if seen.get(temp) is not None:
                return {seen[temp], i}
            else:
                seen[nums[i]] = i