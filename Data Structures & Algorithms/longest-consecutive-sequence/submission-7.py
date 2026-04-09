class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        res = 0
        for i, item in enumerate(nums):
            # check if it's start of the seq 
            if (item - 1) not in nums:
                length = 0
                while item + length in nums:
                    length += 1
                res = max(length, res)
        return res
