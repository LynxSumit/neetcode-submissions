class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
                i = 0
                j = len(row) - 1
                while i <= j:
                    mid = (j+i) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        j = mid - 1
                    else:
                        i = mid + 1
        return False