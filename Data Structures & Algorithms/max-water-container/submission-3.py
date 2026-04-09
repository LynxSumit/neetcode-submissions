class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float('-inf')
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                lowest = min(heights[i], heights[j])
                res = max(res, (j-i) * lowest)
        return res
            