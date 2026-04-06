class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i= 0
        j = len(numbers)-1
        indexes = []
        while(True):
            result = numbers[i] + numbers[j]
            if(result> target):
                j-=1
                continue

            elif(result<target):
                i+=1
                continue
            
            indexes.append(i+1)
            indexes.append(j+1)
            return indexes