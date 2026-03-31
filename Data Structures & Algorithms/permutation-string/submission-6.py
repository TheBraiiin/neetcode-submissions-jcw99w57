class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        l, r = 0, 0
        
        for c in s1:
            s1_arr[ord(c) - ord('a')] += 1

        while r < len(s2):
            s2_arr[ord(s2[r]) - ord('a')] += 1

            if s1_arr == s2_arr:
                return True
            
            if r - l + 1 == len(s1):
                s2_arr[ord(s2[l]) - ord('a')] -= 1
                l += 1

            r += 1    

        return False    