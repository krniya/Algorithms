def final_string(typed_word: str) -> str:
    """Generate word with faulty key "i"

    Args:
        typed_word (str): _description_

    Returns:
        str: _description_
    """
    stack = []
    FAULTY_KEY = 'i'
    for character in typed_word:
        if character != FAULTY_KEY:
            stack.append(character)
            continue
        stack.reverse()
    return "".join(stack)
