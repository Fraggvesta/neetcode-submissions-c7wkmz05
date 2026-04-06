class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while(start <= end):
            m = int((end+start)/2)
            if(nums[m]<target):
                start = m+1
            elif nums[m]>target:
                end = m - 1
            elif nums[m] == target:
                return m
            
        return -1
