class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_count = set()

        for num in nums:
            num_count.add(num)

        res = 0

        for num in nums:
            curr = 0
            lnum = num - 1
            while lnum in num_count:
                curr += 1
                res = max(curr, res)
                num_count.remove(lnum)
                lnum -= 1

            while num in num_count:
                curr += 1
                res = max(curr, res)
                num_count.remove(num)
                num += 1
        
        return res
            