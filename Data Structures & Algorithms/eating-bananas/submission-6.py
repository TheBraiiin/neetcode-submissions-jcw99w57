class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            ate = self.eat(piles, m)
            if ate <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res

    def eat(self, piles, pace):
        curr = 0
        for pile in piles:
            curr += math.ceil(pile / pace)
        
        return curr