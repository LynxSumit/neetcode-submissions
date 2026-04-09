class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, output = 1, [] 
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num
        if zero_cnt > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if zero_cnt > 0:
                output.append(prod if nums[i] == 0 else 0)
            else:
                output.append(prod // nums[i])
        return output