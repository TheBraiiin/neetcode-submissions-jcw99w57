class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        l = r = res = count = 0

        while r < len(s):
            while r < len(s) and s[r] in sset:
                count -= 1
                sset.remove(s[l])
                l += 1

            sset.add(s[r])
            count += 1
            r += 1
            res = max(res, count)

        return res

        
        