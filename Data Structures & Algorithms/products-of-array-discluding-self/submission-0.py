class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l_product = [0] * len(nums)
        r_product = [0] * len(nums)

        curr_l = 1
        for i in range(0, len(nums), 1):
            curr_l *= nums[i]
            l_product[i] = curr_l

        curr_r = 1
        for i in range(len(nums) - 1, -1, -1):
            curr_r *= nums[i]
            r_product[i] = curr_r

        print(l_product)
        print(r_product)

        res = []
        for i in range(len(nums)):
            l = 1
            r = 1

            if i != 0: 
                l = l_product[i - 1]
            if i != len(nums) - 1:
                r = r_product[i + 1]

            res.append(l * r)

        return res

