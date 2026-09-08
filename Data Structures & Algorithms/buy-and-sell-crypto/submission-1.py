class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0 , 1
        max_profit = 0

        print(l,r)

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                max_profit = max(prices[r]-prices[l], max_profit)
                r += 1
        
        return max_profit