def discountPrices(sentence: str, discount: int) -> str:
        words = sentence.split()
        for i, word in enumerate(words):
            if len(word) > 1 and word[0] == '$' and word[1 :].isnumeric():
                words[i] = f'${float(word[1 :]) * (1 - discount / 100):.2f}'
        return ' '.join(words) 