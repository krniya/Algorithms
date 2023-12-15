from typing import List


def destCity(paths: List[List[str]]) -> str:
        start_cities, end_cities = map(set, zip(*paths))
        destination = (end_cities - start_cities).pop()
        return destination