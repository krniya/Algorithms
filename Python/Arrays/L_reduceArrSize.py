from collections import Counter


def minSetSize(arr) -> int:
        n = len(arr)
        cnt = Counter(arr)

        counting = [0] * (n + 1)
        for freq in cnt.values():
            counting[freq] += 1

        ans, removed, half, freq = 0, 0, n // 2, n
        while removed < half:
            ans += 1
            while counting[freq] == 0: freq -= 1
            removed += freq
            counting[freq] -= 1
        return ans