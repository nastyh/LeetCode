class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        p,f = 0,0 # previous, following
        for i, c in enumerate(flowerbed):
                f = 0 if i + 1 >= len(flowerbed) else flowerbed[i+1]
                if p == c == f == 0:
                    flowers += 1
                    p = 1
                else:
                    p = c
        return flowers >= n
