class Solution:
    def trap(self, height: List[int]) -> int:
        water_stored, total_stored = [], 0
        for i in range(len(height)):
            left, right, mx_left, mx_right = i, i, 0, 0
            while left >= 0:
                mx_left = max(mx_left, height[left])
                left -= 1
            while right < len(height):
                mx_right = max(mx_right, height[right])
                right += 1
            lowest = min(mx_left, mx_right)
            if lowest < 0:
                water_stored.append(0)
            else:
                water_stored.append(lowest - height[i])
        for unit in water_stored:
            total_stored += unit
        return total_stored
