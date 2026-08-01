class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]

            robbed = nums[i] + dfs(i + 2)
            not_robbed = dfs(i + 1)

            most_money = max(robbed, not_robbed)

            memo[i] = most_money

            return most_money

        return dfs(0)