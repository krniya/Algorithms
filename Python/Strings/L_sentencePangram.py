def checkIfPangram(sentence: str) -> bool:
        checked = set()
        for ch in sentence:
            checked.add(ch)
        return len(checked) == 26