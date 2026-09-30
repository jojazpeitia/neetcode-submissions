class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 1. run binary search on the rows (top to bottom)
        # if no row is found return false!

        # 2. run binary search on the row that was found
        # if value not found return false, else return true

        rows, columns = len(matrix), len(matrix[0])

        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom -= 1
            elif target > matrix[row][-1]:
                top += 1
            else:
                break

        if bottom < top: return False

        # row = (top + bottom) // 2
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r -= 1
            elif target > matrix[row][m]:
                l += 1

        return False

                



        

