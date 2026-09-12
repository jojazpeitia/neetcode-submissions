class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # monotized stack approach !!

        ans = [0] * len(temperatures)

        stack = []

        for index, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                pop = stack.pop()
                pop_index = pop[0]
                pop_value = pop[1]

                ans[pop_index] = index - pop_index

            stack.append([index, value])

        return ans


        

        