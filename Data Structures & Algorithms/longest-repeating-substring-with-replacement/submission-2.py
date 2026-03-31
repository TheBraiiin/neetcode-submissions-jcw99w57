class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)

        l, r, res, max_c = 0, 0, 0, 0

        while r < len(s):
            dic[s[r]] += 1
            max_c = max(max_c, dic[s[r]])

            if r - l + 1 - max_c > k:
                dic[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res

