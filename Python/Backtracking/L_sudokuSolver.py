from collections import defaultdict

def solveSudoku(board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        
        q = []
        vals = [str(n) for n in range(1, 10)]

        for r in range(9):
            for c in range(9):
                if (v := board[r][c]) == '.':
                    q.append((r, c))
                else:
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[(r//3, c//3)].add(v)

        def dfs():
            if not q:
                return True
            r, c = q.pop()
            b = (r//3, c//3)
            for v in vals:
                if v not in rows[r] and v not in cols[c] and v not in boxes[b]:
                    board[r][c] = v
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[b].add(v)
                    if dfs():
                        return True
                    board[r][c] = '.'
                    rows[r].remove(v)
                    cols[c].remove(v)
                    boxes[b].remove(v)
            q.append((r, c))
            return False

        dfs()