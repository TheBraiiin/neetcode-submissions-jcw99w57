class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (r + l) // 2
            if self.eatBananas(piles, m, h):
                res = m
                r = m - 1
            else:
                l = m + 1

        return piles[-1] if res == 100000000 else res
        
    def eatBananas(self, piles, pace, h):
        curr = 0
        for pile in piles:
            curr += math.ceil(pile / pace)
        
        return curr <= h

    # 7

    # 1, 2, 3, 4

    # 9


    # 4, 10, 23, 25

    # 1 + 1  + 3 + 3