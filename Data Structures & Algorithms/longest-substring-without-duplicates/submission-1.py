class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        letters = set()
        res = 1
        l, r = 0, 0

        while r < len(s):
            if s[r] not in letters:
                letters.add(s[r])
                res = max(res, len(letters))
                r += 1
            else:
                letters.remove(s[l])
                l += 1
        return res
                #z x y z x y z
                #.   l
                #.       r
                #z x y y x y z
                #.       l
                #.           r

              # a b c a b c b b
                    # l
                    #       r

                    # c, a, b