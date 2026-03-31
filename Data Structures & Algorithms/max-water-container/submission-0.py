class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if len(heights) == 2: 
                return min(heights[0], heights[1])
        
        res = 1
        l, r = 0, len(heights) - 1

        while l < r:
                lheight = heights[l]        
                rheight = heights[r]        
                area = min(lheight, rheight) * (r - l)
                res = max(res, area)
                if lheight <= rheight:
                        l+=1
                else:
                        r-=1

        return res                
        #          |
        #.     |.  |
        #      |.  |
        #  |   |.  |