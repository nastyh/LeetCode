class Solution:
    def largestInteger(self, num: int) -> int:
        """
        O(nlogn) to sort
        O(n) to store the numbers
        Cut the number into digits
        Store even and odds in the respective lists: from the largest to the smallest
        Traverse the original
        If the first digit is even, take the largest from the even list, move the pointer
        And similarly with odds
        Rebuild the answer 
        """
        all_nums = [int(d) for d in str(num)]
        odd_digits = sorted([int(d) for d in str(num) if int(d) % 2 == 1], reverse=True)
        even_digits = sorted([int(d) for d in str(num) if int(d) % 2 == 0], reverse=True)
        print(odd_digits)
        print(even_digits)
        res = []
        odd_ix, even_ix = 0, 0 
        for n in all_nums:
            if n % 2 == 0:
                res.append(even_digits[even_ix])
                even_ix += 1
            else:
                res.append(odd_digits[odd_ix])
                odd_ix += 1
        return int("".join(map(str, res)))
        