def largestGoodInteger(num: str) -> str:
    largest_number = ""
    for i in range(1,len(num) - 1):
        if num[i-1] == num[i] == num[i+1]:
            largest_number = max(largest_number, num[i])
    return largest_number * 3