import collections


def bagOfTokensScore(tokens , power: int) -> int:
        res = cur = 0
        d = collections.deque(sorted(tokens))
        while d and (d[0] <= power or cur):
            if d[0] <= power:
                power -= d.popleft()
                cur += 1
            else:
                power += d.pop()
                cur -= 1
            res = max(res, cur)
        return res