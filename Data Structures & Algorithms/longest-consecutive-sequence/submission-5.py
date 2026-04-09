class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        store = []
        longest = 0
        print(nums)
        for i, item in enumerate(nums):
            print(store, item)
            if len(store) == 0:
                store.append(item)
            else:
                if item - store[-1] == 1:
                    store.append(item)
                else:
                    store = [item]
            longest = max(len(store), longest)
        return longest


        
