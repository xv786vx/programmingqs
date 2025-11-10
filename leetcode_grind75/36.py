# 36 Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in '123456789' and board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                elif board[i][j] in rows[i]:
                    return False

                if board[j][i] in '123456789' and board[j][i] not in cols[i]:
                    cols[i].add(board[j][i])
                elif board[j][i] in cols[i]:
                    return False
                
                if board[i][j] in '123456789' and board[i][j] not in blocks[i // 3][j // 3]:
                    blocks[i // 3][j // 3].add(board[i][j])
                elif board[i][j] in blocks[i // 3][j // 3]:
                    return False
        
        return True