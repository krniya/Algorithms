import collections


def isValidSudoku(board):
    return (is_row_valid(board) and
            is_col_valid(board) and
            is_square_valid(board))


def is_row_valid(board):
    for row in board:
        if not is_unit_valid(row):
            return False
    return True


def is_col_valid(board):
    for col in zip(*board):
        if not is_unit_valid(col):
            return False
    return True


def is_square_valid(board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y]
                      for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_unit_valid(square):
                return False
    return True


def is_unit_valid(unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)


def isValidSudoku(board) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squr = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                curr = board[r][c]
                if curr in rows[r] or curr in cols[c] or curr in squr[(r//3, c//3)]:
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                squr[(r//3, c//3)].add(curr)
        return True


print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

