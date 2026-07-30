class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -1001
        count = 0

        for i in range(len(nums)):
            if count < 0:
                count = 0
            count += nums[i]
            res = max(count, res)
                
        return res
                
            

            