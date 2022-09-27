def pushDominoes(dominoes: str) -> str:
        n = len(dominoes)
        r_dist = [0 if d == 'R' else float('inf') for d in dominoes]
        l_dist = [0 if d == 'L' else float('inf') for d in dominoes]
        ri = float('inf')
        for i, d in enumerate(dominoes):
            if d == 'R':
                ri = i
            elif d == '.' and ri != float('inf'):
                r_dist[i] = i - ri
            elif d == 'L':
                ri = float('inf')
        li = float('inf')
        for i, d in reversed(list(enumerate(dominoes))):
            if d == 'L':
                li = i
            elif d == '.' and li != float('inf'):
                l_dist[i] = li - i
            elif d == 'R':
                li = float('inf')
            
        res = ''
        for i, d in enumerate(dominoes):
            if d == '.' and r_dist[i] != l_dist[i]:
                res += 'R' if r_dist[i] < l_dist[i] else 'L'
            else:
                res += d
        return res