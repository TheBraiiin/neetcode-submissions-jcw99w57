class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kmap = {}

        for num in nums:
            kmap[num] = kmap.get(num, 0) + 1

        arr = [[] for _ in range(len(nums) + 1)]

        for key in kmap:
            value = kmap[key]
            if arr[value] is None:
                arr[value] = []
            arr[value].append(key)

        res = []

        for i in range(len(arr) - 1, 0, -1):
            curr_list = arr[i]
            j = 0
            while len(res) < k and j < len(curr_list):
                res.append(curr_list[j])
                j+=1

        return res