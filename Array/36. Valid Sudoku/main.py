"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        area = [{} for _ in range(9)]

        area_index_dict = {
            0: {0: 0, 1: 1, 2: 2},
            1: {0: 3, 1: 4, 2: 5},
            2: {0: 6, 1: 7, 2: 8}
        }

        for i in range(9):
            for j in range(9):
                cur_ele = board[i][j]
                if cur_ele == '.':
                    continue    
                else:
                    if cur_ele in row[i]:
                        return False
                    else:
                        row[i][cur_ele] = 1

                    if cur_ele in col[j]:
                        return False
                    else:
                        col[j][cur_ele] = 1
                    
                    area_id  =  area_index_dict[i//3][j//3]
                    if cur_ele in area[area_id]:
                        return False
                    else:
                        area[area_id][cur_ele] = 1
        return True

        


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    sol = Solution()
    res = sol.isValidSudoku(board)
    print(res)