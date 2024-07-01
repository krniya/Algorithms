def threeConsecutiveOdds(arr) -> bool:
    def is_odd(n):
        return n % 2
    for i in range(len(arr) - 2):
        if is_odd(arr[i]) and is_odd(arr[i+1]) and is_odd(arr[i+2]):
            return True
    return False