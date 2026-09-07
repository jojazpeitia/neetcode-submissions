class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maxL, maxR = height[l], height[r]

        total = 0
        
        while l < r:
            if maxL <= maxR:
                l += 1
                if maxL - height[l] > 0:
                    total += maxL - height[l]
                maxL = max(maxL, height[l])
            else:
                r -= 1
                if maxR - height[r] > 0:
                    total += maxR - height[r]
                maxR = max(maxR, height[r])

        return total