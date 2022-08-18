from collections import deque


def findItinerary(tickets):
        nei = { u: deque for u, _ in tickets}
        res = ["JFK"]
        tickets.sort()
        for u, v in tickets:
            nei[u].append(v)
        def dfs(curr):
            if len(res) == len(tickets) + 1:
                return True
            if curr not in nei:
                return False
            temp = list(nei[curr])
            for v in temp:
                nei[curr].popleft()
                res.append(v)
                if dfs(v):
                    return True
                res.pop()
                nei[curr].append(v)
            return False
        dfs("JFK")
        return res