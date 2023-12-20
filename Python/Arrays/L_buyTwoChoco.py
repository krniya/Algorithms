from typing import List


def buyChoco(prices: List[int], money: int) -> int:
    first_min_cost = second_min_cost = float("inf")

    for p in prices:
        if p < first_min_cost:
            second_min_cost, first_min_cost = first_min_cost, p
        else:
            second_min_cost = min(second_min_cost, p)

    leftover = money - (first_min_cost + second_min_cost)

    return leftover if leftover >= 0 else money