class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            if self.eatBananas(piles, h, m):
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        
        return res

    def eatBananas(self, piles, h, pace):
        curr = 0
        for pile in piles:
            curr += math.ceil(pile / pace)

        return curr <= h