class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] < nums[j]:
                res = min(res, nums[i])
                break
            mid = (i+j) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[i]:
                i = mid + 1
            else:
                j = mid - 1
        return res