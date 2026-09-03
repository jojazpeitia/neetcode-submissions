class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans= []

        print(nums)
        
        for index, value in enumerate(nums):

            if index == 0 or nums[index - 1] != nums[index]:

                l = index + 1
                r = len(nums) - 1

                while l < r:
                    if nums[index] + nums[l] + nums[r] == 0:
                        ans.append([nums[index], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                    elif nums[index] + nums[l] + nums[r] < 0:
                        l += 1
                    else:
                        r -= 1

        return ans



            
        