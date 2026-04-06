from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r

        while(l <= r):
            m =(r + l)//2
            hours = 0
            for i in piles:
                hours+= ceil(i/m)

            if hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
