def largestAltitude(gains) -> int:
        largestAlt = currentAlt = 0
        for gain in gains:
            currentAlt += gain
            largestAlt = max(currentAlt, largestAlt)
        return largestAlt