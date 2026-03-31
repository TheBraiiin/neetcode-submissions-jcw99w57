class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temperatures[stack[-1]] < temp:
                lower_temp = stack.pop()
                res[lower_temp] = i - lower_temp

            stack.append(i)

        return res
                #30,38,30,36,35,40,28
                                #  i
                #
                # 4
                # 3
                # 1

                # 1, ,1 