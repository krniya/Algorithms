def kidsWithCandies(candies, extraCandies: int):
        max_candies = max(candies)
        for i in range(len(candies)):
            candies[i] = (candies[i] + extraCandies >= max_candies)
        return candies