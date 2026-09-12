class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the listed!!

        nums.sort()
        ans = []
        print(nums)

        for index, value in enumerate(nums):
            if index == 0 or value != nums[index - 1]:
                # do two sum on the rest!
                l = index + 1
                r = len(nums) - 1
                
                while l < r:
                    if nums[index] + nums[l] + nums[r] == 0:
                        ans.append([ nums[index], nums[l], nums[r] ])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                    elif nums[index] + nums[l] + nums[r] < 0:
                        l += 1
                    elif nums[index] + nums[l] + nums[r] > 0:
                        r -= 1

        return ans
                    

                    


        