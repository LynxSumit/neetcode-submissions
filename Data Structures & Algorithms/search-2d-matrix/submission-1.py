class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for el in matrix:
        #     for num in el:
        #         if num == target:
        #             return True   
        # return False # O(N * M)

        for row in matrix:
            start = 0
            end= len(row) - 1
            while(start <= end):
                mid = (end+start) // 2
                if row[mid] > target :
                    end = mid - 1
                elif row[mid] < target:
                    start = mid + 1
                else:
                    return True
        return False