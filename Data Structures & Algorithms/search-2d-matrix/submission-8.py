class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
                
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (r + l) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                break
        return self.bin_search(matrix[r], target)


    def bin_search(self, arr, target):
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (r + l) // 2
            if arr[m] == target:
                return True
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return False




