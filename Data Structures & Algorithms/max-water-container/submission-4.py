class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float("-inf")
        i, j = 0, len(heights) - 1
        while i <= j:
            lowest = min(heights[i], heights[j])
            res = max(res, lowest * (j-i))
            if lowest == heights[i]:
                i+=1
            else:
                j-=1
        return res