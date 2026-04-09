class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 
        n = len(height)
        left_mx = [0] * n
        right_mx = [0] * n

        left_mx[0] = height[0]
        for i in range(1, n):
            left_mx[i] = max(left_mx[i - 1], height[i])

        right_mx[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_mx[i] = max(right_mx[i + 1], height[i])
        res = 0
        for i in range(n):
            res += min(left_mx[i], right_mx[i]) - height[i]
        return res
