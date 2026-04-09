class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        longest = 0
        for i in range(len(nums)):
            store = []
            for j in range(i, len(nums)):
                if len(store) == 0:
                    store.append(nums[j])
                else:
                    if nums[j] - store[-1] == 1:
                        store.append(nums[j])
            longest = max(longest, len(store))
        return longest 
