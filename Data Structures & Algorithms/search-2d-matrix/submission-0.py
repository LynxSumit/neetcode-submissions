class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for el in matrix:
            for num in el:
                if num == target:
                    return True   
        return False