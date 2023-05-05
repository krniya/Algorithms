def maxVowels(s: str, k: int) -> int:
        noOfVow = left = maxVow = 0
        vowels = set(["a","e","i","o","u"])
        for right, ch in enumerate(s):
            if right - left >= k:
                if s[left] in vowels:
                    noOfVow -= 1
                left += 1
            if ch in vowels:
                noOfVow += 1
            maxVow = max(maxVow, noOfVow)
        return maxVow