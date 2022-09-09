def numberOfWeakCharacters(properties) -> int:
        properties.sort(key= lambda x: (-x[0], x[1]))
        count = 0
        maxDef = float("-inf")
        for attack, defense in properties:
            if defense < maxDef:
                count += 1
            maxDef = max(maxDef, defense)
        return count