class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_maps= {}
        for i, item in enumerate(nums):
            if target - item in target_maps and nums[target_maps.get(target - item)] + item == target:
                smaller = min(target_maps[target-item], i)
                larger = max(target_maps[target-item], i)
                return [smaller, larger]
            else:
                target_maps[item] = i
        return [-1,-1]