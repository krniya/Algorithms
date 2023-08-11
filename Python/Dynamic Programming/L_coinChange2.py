from typing import List


def change(amount: int, coins: List[int]) -> int:
    change_method_count = [1] + [ 0 for _ in range(amount)]
    for cur_coin in coins:
        for small_amount in range(cur_coin, amount+1):
            change_method_count[small_amount] += change_method_count[small_amount - cur_coin]
    return change_method_count[amount]