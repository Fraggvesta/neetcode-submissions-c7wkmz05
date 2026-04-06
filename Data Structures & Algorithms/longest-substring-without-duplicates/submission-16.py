class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        b = 0
        max_len = 0
        letters = dict()
        for i,j in enumerate(s):
            if j in letters and letters[j] >= b:
                b = letters[j] + 1
            
            letters[j] = i
            max_len = max(max_len, i - b + 1)
                

        return max_len