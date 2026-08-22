class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        max_p,p = 0,0
        while r < len(prices):
            if prices[l]>prices[r]:
                l=r
            p = prices[r]-prices[l]
            max_p = max(max_p, p)
            r+=1
        return max_p