class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(len(prices)):

            while prices[l] > prices[r]:
                l += 1
            
            profit = abs(prices[l] - prices[r])

            maxP = max(maxP, profit)
        
        return maxP