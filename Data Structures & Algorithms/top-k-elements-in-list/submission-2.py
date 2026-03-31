class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            freq[value].append(key)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            curr_lst = freq[i]
            j = 0
            while len(res) < k and j < len(curr_lst):
                res.append(curr_lst[j])
                j+=1

        return res

