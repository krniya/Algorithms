class sol:
    def getMinDiff(self, arr, n, k):
        if n == 1:
            return 0
        arr.sort()
        diff = arr[n-1] - arr[0]
        mini = arr[0]+k
        maxi = arr[n-1]-k
        if mini > maxi:
            mini, maxi = maxi, mini
        for i in range(n-1):
            d = arr[i] - k
            s = arr[i] + k
            if d >= mini or s <= maxi:
                continue
            if (maxi - d) <= (s - mini):
                mini = d
            else:
                maxi = s
        return min(diff, maxi - mini)


solo = sol()
print(solo.getMinDiff([6, 1, 9, 1, 1, 7, 9, 5, 2, 10], 10, 4))
