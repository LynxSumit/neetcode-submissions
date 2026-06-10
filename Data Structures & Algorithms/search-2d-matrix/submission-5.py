class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        row = None
        while top <= bottom:
            mid = (bottom + top) // 2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                row = matrix[mid]
                break
        if row == None:
            return False
        print(row)
        i, j = 0, cols - 1
        while i <= j:
            mid = (i+j) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                j = mid - 1
            else:
                i = mid+1
        return False


                
