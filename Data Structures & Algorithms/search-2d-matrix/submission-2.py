class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for el in matrix:
        #     for num in el:
        #         if num == target:
        #             return True   
        # return False # O(N * M)

        # for row in matrix:
        #     start = 0
        #     end= len(row) - 1
        #     while(start <= end):
        #         mid = (end+start) // 2
        #         if row[mid] > target :
        #             end = mid - 1
        #         elif row[mid] < target:
        #             start = mid + 1
        #         else:
        #             return True
        # return False. # O(N * Log(M) )
            row_st, row_en = 0, len(matrix) - 1 
            # Step 1: Binary search on rows to find the correct row
            while row_st <= row_en:
                mid_row = (row_st + row_en) // 2  # Middle row
                if target > matrix[mid_row][-1]:  # Target is greater than the largest element in the row
                    row_st = mid_row + 1
                elif target < matrix[mid_row][0]:  # Target is smaller than the smallest element in the row
                    row_en = mid_row - 1
                else:
                    break  # Target must be in this row

            # If no valid row is found
            if not (row_st <= row_en):
                return False

            # Narrowed down to the correct row
            mid_row = (row_st + row_en) // 2

            # Step 2: Binary search on columns within the identified row
            col_start, col_end = 0, len(matrix[mid_row]) - 1
            while col_start <= col_end:
                mid_col = (col_start + col_end) // 2  # Middle column
                if target > matrix[mid_row][mid_col]:  # Target is in the right half
                    col_start = mid_col + 1
                elif target < matrix[mid_row][mid_col]:  # Target is in the left half
                    col_end = mid_col - 1
                else:
                    return True  # Target found

            # Target not found
            return False


