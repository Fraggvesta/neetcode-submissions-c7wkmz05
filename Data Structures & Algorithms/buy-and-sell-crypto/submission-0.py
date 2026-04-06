class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(0, len(prices)-1):
            j = i+1
            while(j!= len(prices) and prices[j]-prices[i]>0):
                result = max(result, prices[j]-prices[i])
                j+=1
            
        return result
