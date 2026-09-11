class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # O(1) space complexitiy solution
        # fill out pre fix array 1 pass from left to right
        # then from right to left get post fix and multiply against holded pre fix value

        # print(nums)
        prefix = 1
        ans =[]

        for i in nums:
            ans.append(prefix)
            prefix *= i
            
        # print(ans)
        postfix = 1
        # for index, value in enumerate(reversed(ans)):
            # print(index, value)
            # ans[index] = value * postfix
            # postfix *= nums[index]

        r = len(ans)

        while r > 0:
            r-=1
            
            ans[r] *= postfix
            postfix *= nums[r]

        return ans 


        