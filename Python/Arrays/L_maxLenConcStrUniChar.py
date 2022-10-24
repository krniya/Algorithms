def maxLength(A) -> int:
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)


def maxLength(arr) -> int:
        n = len(arr)
        ans = 0
        for mask in range(1 << n):
            seen = set()
            isValid = True
            strSize = 0
            for i in range(n):
                if (mask >> i) & 1 == 0: continue
                for c in arr[i]:
                    if c in seen:   # If c is already existed then it's invalid subsequence.
                        isValid = False
                        break
                    seen.add(c)  # mark as character `c` is already seen
                    strSize += 1
                if not isValid: break  # prune when there is a duplicate
            if isValid and strSize > ans:
                ans = strSize
        return ans