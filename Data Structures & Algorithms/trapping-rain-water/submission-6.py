class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_mx = height[left]
        right_mx = height[right]
        res = 0
        while left < right:
            if left_mx < right_mx:
                left += 1
                left_mx = max(left_mx, height[left])
                res += left_mx - height[left]
            else:
                right -= 1
                right_mx = max(right_mx, height[right])
                res += right_mx - height[right]
        return res







        