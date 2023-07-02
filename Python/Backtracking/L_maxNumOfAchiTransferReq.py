def maximumRequests(n: int, requests) -> int:
        empInBuilding = [0] * n
        maxApproval = 0
        def backtrack(i, approvedReq):
            nonlocal maxApproval
            if i == len(requests):
                if empInBuilding.count(0) == n:
                    maxApproval = max(maxApproval, approvedReq)
                return
            backtrack(i+1, approvedReq)
            empInBuilding[requests[i][0]] -= 1
            empInBuilding[requests[i][1]] += 1
            backtrack(i+1, approvedReq + 1)
            empInBuilding[requests[i][0]] += 1
            empInBuilding[requests[i][1]] -= 1
            
        backtrack(0,0)
        return maxApproval