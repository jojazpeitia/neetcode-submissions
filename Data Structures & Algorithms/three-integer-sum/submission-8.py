class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 0(n * log n)
        nums.sort()
        print(nums)

        # for every distinct 1st number, we apply two sum II on the other 2 numbers
        # when applying two sum II on the other 2 numbers, we have to make sure the 1st number is unique
        # ^ to avoid duplicate answer

        triplets = []

        i = 0
        while i + 2 < len(nums):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

            i += 1
            while i + 2 < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return triplets

        