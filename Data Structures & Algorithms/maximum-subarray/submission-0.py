class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # kadane's algorithm!
        # [-2, 1, -3, 4, -1, 2, 1, -5, -4]
        # we use a prefix in order to restart?
        # ^ furthermore, it can be as simple as whenever prefix is negative, we restart the slidingwindow

        l = 0
        r = 0
        cur = 0
        maximum = float("-infinity")

        while r < len(nums):
            cur += nums[r]
            maximum = max(maximum, cur)
            r += 1
            if cur < 0:
                l = r
                cur = 0
        return maximum








        