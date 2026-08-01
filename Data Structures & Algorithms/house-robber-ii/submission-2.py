class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [[0] * 2 for _ in range(len(nums))]

        def dfs(i, isFirst):
            if i >= len(nums) or isFirst and i == len(nums) - 1:
                return 0
            
            if memo[i][isFirst]:
                return memo[i][isFirst]

            robbed = nums[i] + dfs(i + 2, isFirst)
            not_robbed = dfs(i + 1, isFirst)

            memo[i][isFirst] = max(robbed, not_robbed)
            return memo[i][isFirst]

        return max(dfs(0, True), dfs(1, False))
