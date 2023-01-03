def detectCapitalUse(word: str) -> bool:
        def check(alpha):
            if alpha == "cap":
                for ch in word[1:]:
                    if not ch.isupper():
                        return False
            else:
                for ch in word[1:]:
                    if not ch.islower():
                        return False
            return True
        if word[0].islower():
            return check("low")
        else:
            if len(word) > 1 and word[1].isupper():
                return check("cap")
            else:
                return check("low")