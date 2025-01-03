from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        grids = defaultdict(set)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == ".":
                    continue

                if (
                    board[y][x] in seen_rows[y]
                    or board[y][x] in seen_cols[x]
                    or board[y][x] in grids[y // 3, x // 3]
                ):
                    return False

                seen_rows[y].add(board[y][x])
                seen_cols[x].add(board[y][x])
                grids[y // 3, x // 3].add(board[y][x])

        return True


solution = Solution()
falseInput = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(solution.isValidSudoku(falseInput))

falseInput = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "5", ".", ".", ".", ".", "6", "."],
    ["5", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", "9", ".", "8", ".", ".", "1", "9"],
]
print(solution.isValidSudoku(falseInput))
