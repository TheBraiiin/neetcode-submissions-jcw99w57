class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sps = []

        for i in range(len(position)):
            sps.append((position[i], speed[i]))
        
        sps.sort()
        fleet = 0
        prev = 0
        while sps:
            p, s = sps[-1]

            if (target - p) / s > prev:
                fleet += 1 
                prev = (target - p) / s

            
            sps.pop()

        return fleet

   
            
