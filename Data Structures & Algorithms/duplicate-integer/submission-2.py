class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for num in nums:
            print(num, res)
            if res.get(num):
                return True
            res[num] = True
        return False