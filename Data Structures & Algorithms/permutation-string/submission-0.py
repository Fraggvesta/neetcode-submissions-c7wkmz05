import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        windowsize = 0
        abc1 = {letter: 0 for letter in string.ascii_lowercase}
        abc2 = {letter: 0 for letter in string.ascii_lowercase}

        for i in s1:
            abc1[i] += 1
        
        for i, k in enumerate(s2):
            abc2[k] += 1
            if i+1 > len(s1):
                abc2[s2[i-len(s1)]] -= 1
            if abc1 == abc2:
                return True
        
        return False