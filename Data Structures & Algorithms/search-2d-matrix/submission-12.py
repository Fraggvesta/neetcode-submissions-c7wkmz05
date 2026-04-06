class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = 0
        rowpos = 0
        end = len(matrix[0])-1
        while(rowpos<=end and col < len(matrix)):
            if col+1 != len(matrix) and matrix[col+1][0]<target:
                col+=1
                rowpos = 0
                end = len(matrix[0]) - 1

            if col+1 != len(matrix) and matrix[col+1][0] == target:
                    return True

            m = int((rowpos + end)/2)
            if matrix[col][m] < target:
                rowpos = m + 1
            elif matrix[col][m] > target:
                end = m - 1
            
            elif matrix[col][m] == target:
                return True

        return False