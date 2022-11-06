def orderlyQueue(S: str, K: int) -> str:
        if K > 1: return "".join(sorted(S))
        return min(S[i:]+S[:i] for i in range(len(S)))