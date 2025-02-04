from collections import defaultdict
import math
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue
                # square_index = math.floor(i / 3) * 3 + math.floor(j / 3)
                square_index = (i // 3) * 3 + (j // 3)
                if (
                    cell in rows[i]
                    or cell in columns[j]
                    or cell in squares[square_index]
                ):
                    return False
                rows[i].add(cell)
                columns[j].add(cell)
                squares[square_index].add(cell)
        return True


board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
sol = Solution()
print(sol.isValidSudoku(board))
