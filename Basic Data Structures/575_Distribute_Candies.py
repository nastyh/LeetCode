def distributeCandies(candies):
    return min(len(set(candies)), len(candies)//2)
