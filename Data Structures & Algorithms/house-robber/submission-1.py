class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        memo = [-1] * len(nums)

        def dfs(i, count):
            nonlocal res

            if i >= len(nums):
                return
            
            curr_count = count + nums[i]
            
            if memo[i] != -1 and memo[i] >= curr_count:
                return

            memo[i] = curr_count

            res = max(curr_count, res)

            dfs(i + 2, curr_count)
            dfs(i + 3, curr_count)

        for i in range(len(nums)):
            dfs(i, 0)

        return res
