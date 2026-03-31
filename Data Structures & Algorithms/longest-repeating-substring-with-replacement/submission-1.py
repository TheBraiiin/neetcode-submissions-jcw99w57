class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l, r, max_freq, res = 0, 0, 0, 0

        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res


        # k = 2
        # A A A B A B B B B B
        # A : 2 
        # B : 6
        # m : 6