class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        l = 0
        r = len(s) - 1

        while l < r:
            while not self.isAlphanumeric(s[l]):
                if l >= r:
                    break
                l+=1
            while not self.isAlphanumeric(s[r]) and l < r:
                if l >= r:
                    break
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True
    
    def isAlphanumeric(self, c):
        return '0' <= c <= '9' or 'A' <= c <= 'Z' or 'a' <= c <= 'z'
