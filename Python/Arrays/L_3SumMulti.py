from collections import Counter
from itertools import combinations_with_replacement

def threeSumMulti(arr, target):
    cnt, ans = Counter(arr), 0
    for i in cnt:
        for j in cnt:
            k = target - i - j
            if i == j == k:
                ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
            elif i == j:
                ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[k]
            elif i < j < k:
                ans += cnt[i] * cnt[j] * cnt[k]
    return ans % (10**9 + 7)

print(threeSumMulti([1,1,2,2,2,2], 5))

# cnt, ans = {}, 0
#     for n in arr:
#         if n not in cnt:
#             cnt[n] = 1
#         else:
#             cnt[n] += 1