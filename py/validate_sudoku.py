class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            row = [item for item in board[i] if item.isnumeric() and 0 < int(item) < 10]
            column = [board[j][i] for j in range(len(board[i])) if board[j][i].isnumeric() and 0 < int(board[j][i]) < 10]

            if len(row) != len(set(row)) or len(column) != len(set(column)):
                return False

        blocks = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [
                    [board[x][y] for y in range(j, j+3)]
                    for x in range(i, i+3)
                ]
                blocks.append(block)

        for block in blocks:
            cube_num = []
            print(block)
            for row in block:
                print(row)
                for item in row:
                    print(item)
                    if item.isnumeric():
                        cube_num.append(item)
            if len(cube_num) != len(set(cube_num)):
                return False

        return True

solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))