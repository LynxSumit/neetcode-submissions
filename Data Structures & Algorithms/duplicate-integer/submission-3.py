class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for i, item in enumerate(nums):
            print(occurences)
            if item in occurences:
                return True
            else:
                if occurences.get(item):
                    occurences[item] += 1
                else:
                    occurences[item] = 1
        return False

        