class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_count = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in num_count:
                curr_len = 1
                while (num + curr_len) in num_count:
                    curr_len += 1
                
                res = max(res, curr_len)
                
        return res

        # for num in nums:
        #     curr = 0
        #     lnum = num - 1
        #     while lnum in num_count:
        #         curr += 1
        #         res = max(curr, res)
        #         num_count.remove(lnum)
        #         lnum -= 1

        #     while num in num_count:
        #         curr += 1
        #         res = max(curr, res)
        #         num_count.remove(num)
        #         num += 1
        
        return res
            