class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        l = 0 
        r = len(heights) - 1
        maximum = 0

        while l < r:
            if heights[l] <= heights[r]:
                maximum = max(maximum, heights[l] * (r - l))
                l += 1
            else:  
                maximum = max(maximum, heights[r] * (r - l))
                r -= 1

        return maximum