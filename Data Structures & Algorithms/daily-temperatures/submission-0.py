class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i, el in enumerate(temperatures):
            current_temp_day_count = 0
            found = False
            for j in range(i + 1, len(temperatures)):  # Start from the next day
                if temperatures[j] > el:  # Check for a warmer day
                    current_temp_day_count = j - i  # Calculate days until warmer
                    found = True
                    break
            if found:
                res.append(current_temp_day_count)
            else:
                res.append(0)
        return res
