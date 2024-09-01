def construct2DArray(self, original, m: int, n: int):
        result = [[] for _ in range(m)]
        i = 0
        match m * n == len(original):
            case True:
                while i < m:
                    result[i] = original[i * n:(i * n + n)]
                    i += 1
            case _:
                return []
        return result