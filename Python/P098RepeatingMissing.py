class Solution:
    def repeatMiss(self, arr):
        t = arr[0]
        h = arr[0]
        while True:
            t = arr[t]
            h = arr[arr[h]]
            if t == h:
                break
        p1 = arr[0]
        p2 = t
        while p1 != p2:
            p1 = arr[p1]
            p2 = arr[p2]
        return [p1, p2]


rm = Solution()

print(rm.repeatMiss([1, 2, 4, 3, 8, 6, 7, 5, 4]))
