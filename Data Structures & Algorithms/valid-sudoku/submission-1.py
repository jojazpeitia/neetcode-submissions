class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        c_dict = defaultdict(list)
        r_dict = defaultdict(list)
        grid_dict = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in c_dict[c]:
                    return False
                else:
                    c_dict[c].append(board[r][c])

                if board[r][c] in r_dict[r]:
                    return False
                else:
                    r_dict[r].append(board[r][c])

                if board[r][c] in grid_dict[r // 3, c // 3]:
                    return False
                else:
                    grid_dict[r // 3, c // 3].append(board[r][c])

        
        return True
        