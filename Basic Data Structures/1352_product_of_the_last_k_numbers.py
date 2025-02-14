class ProductOfNumbers:

    def __init__(self):
        """
        O(1) for each addition and for division, too
        Space is O(n) for the prefix product
        Key here is to store a prefix product list.
        The result is the prod of the last k integers,
        so it's going to be last number // by what is before the 
        k-th element 
        """
        self.l = [1]
        self.res = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.l = [1]
        else:
            self.l.append(self.l[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.l):
            return 0 
        return self.l[-1] // self.l[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)