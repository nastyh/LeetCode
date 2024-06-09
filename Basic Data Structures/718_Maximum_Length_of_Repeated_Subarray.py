def findLength_comments(self, nums1: List[int], nums2: List[int]) -> int:
        """
        # O(nums1 * nums2) both 
        create a 2d dp of the size nums1 times nums2
        it's filled with zeroes first but add on more extra col and row
        It's needed to process the first element and not fall out of bounds
        We will have two for loops 
        We start with (1, 1) and say that if at these indices there is a match,
        we go to our matrix and update the element by taking the value from the prev cell
        and adding one. We look to the prev element b/c it's a subarray, so the matches should be
        next to each other
        And we can update the res here or run max(dp) at the end
        """
        dp = [[0] * (len(nums1) + 1) for _ in range((len(nums2) + 1))]  # A cols, B rows
        res = 0
        for row in range(1, len(nums2) + 1):
            for col in range(1, len(nums1) + 1):
                if nums1[col - 1] == nums2[row - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                    res = max(res, dp[row][col])
        return res
        """
        or we don't need to update res in the loop 
        and can just return at the end:
        return max([max(i) for i in dp])
        internals will return a list with the max value from each row
        and then we take the max value from them 
        """

def findLength(A, B):
    dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    for a_ix in range(len(A)):
        for b_ix in range(len(B)):
            if A[a_ix] == B[b_ix]:
                dp[a_ix][b_ix] = dp[a_ix - 1][b_ix - 1] + 1
    return max([max(i) for i in dp])
    # return dp

 
def findLength_alt(A, B):  # O(AB) both
    dp = [[0] * (len(A) + 1) for _ in range((len(B) + 1))]  # A cols, B rows
    res = 0
    for row in range(1, len(B) + 1):
        for col in range(1, len(A) + 1):
            if A[col - 1] == B[row - 1]:
                dp[row][col] = 1 + dp[row - 1][col - 1]
                res = max(res, dp[row][col])
    return res


def findLength_efficient(A, B):  # O(AB and O(B)
    res = 0
    dp = [[0] * (len(B) + 1) for _ in range(2)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            dp[i % 2][j] = 0
            if A[i - 1] == B[j - 1]:
                dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
                res = max(res, dp[i % 2][j])
    return res 



if __name__ == '__main__':
    print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
    print(findLength_alt([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength_alt([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
    print(findLength_efficient([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(findLength_efficient([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
        
