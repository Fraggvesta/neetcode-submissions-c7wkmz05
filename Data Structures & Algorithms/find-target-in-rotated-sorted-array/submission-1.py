class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)

        # -------- find pivot (smallest element) --------
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        # -------- decide which half to search --------
        if target <= nums[-1]:
            l, r = pivot, n - 1
        else:
            l, r = 0, pivot - 1

        # -------- standard binary search --------
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

        
            