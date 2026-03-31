class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_freq, r, l, res = 0, 0, 0, 0

        while r < len(s):
          counts[s[r]] += 1
          max_freq = max(max_freq, counts[s[r]])
          if (r - l + 1) - max_freq > k:
            counts[s[l]] -= 1
            l += 1
                  
          res = max(res, r - l + 1)
          r += 1

        return res

        # A A A B A B B B B B B
        #    l     
         #             r
        # 0 1 2 3 4 5 6 7 8 9 10
                      