class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * n

        for num in nums:
            arr[num] += 1
        
        for i in range(len(arr)):
            if arr[i] > 1:
                return i
            
        return 0

        