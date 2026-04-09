class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)
        for i in range(n):
            count, j, found = 0, i+1, False
            while j < n:
                if temperatures[j] > temperatures[i]:
                    count += 1
                    found = True
                    break
                else:
                    count += 1
                j+=1
            result.append(count if found else 0)
        return result

