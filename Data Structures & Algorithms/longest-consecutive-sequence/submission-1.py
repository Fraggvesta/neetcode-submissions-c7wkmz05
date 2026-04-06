class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numero = set()
        for i in nums:
            numero.add(i)
        sequences = []
        result = 1
        for i in numero:
            if i-1 not in numero:
                while(True):
                    if(i+1 in numero):
                        i+=1
                        result+=1
                        continue
                    sequences.append(result)
                    result = 1
                    break
        
        return max(sequences)