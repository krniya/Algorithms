def bestClosingTime(customers: str) -> int:
        n = len(customers)
        prefix_n, postfix_y = [0] * (n + 1), [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_n[i] = prefix_n[i-1]
            if customers[i-1] == 'N':
                prefix_n[i] += 1
        for i in range(n-1, -1, -1):
            postfix_y[i] = postfix_y[i+1]
            if customers[i] == 'Y':
                postfix_y[i] += 1
        min_penalty, idx = float("inf"), 0
        for i in range(n+1):
            penalty = prefix_n[i] + postfix_y[i]
            if penalty < min_penalty:
                min_penalty = penalty
                idx = i
        return idx
            