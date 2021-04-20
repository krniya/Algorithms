# O(n) | O(1)
def longestPeek(arr):
    i = 1
    longestpeek = 0
    while i < len(arr) - 1:
        isPeak = arr[i-1] < arr[i] and arr[i] > arr[i+1]
        if not isPeak:
            i += 1
            continue
        left = i - 2
        while left >= 0 and arr[left] < arr[left + 1]:
            left -= 1
        right = i + 2
        while right < len(arr) and arr[right] < arr[right - 1]:
            right += 1
        currentpeek = right - left - 1
        longestpeek = max(longestpeek, currentpeek)
        i = right
    return longestpeek
