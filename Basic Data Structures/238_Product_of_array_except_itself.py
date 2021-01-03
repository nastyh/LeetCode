def productExceptSelf(nums):  # O(N) and O(N)
    """
    Two lists: multiplication of all elements to the left from a current element
    and all elements to the right from a current element
    then multiply respective elements by each other 
    """
    ll, rl = [None] * len(nums), [None] * len(nums)
    ll[0], rl[-1] = 1, 1
    for i in range(1, len(ll)):
        ll[i] = ll[i - 1] * nums[i - 1]
    for j in range(len(rl)-2, -1, -1):
        rl[j] = rl[j + 1] * nums[j + 1]

        """
        or instead of creating rl, we can update ll on the fly:
        right_prod = 1
        for j in range(len(ll) -1 , -1, -1):
            ll[j] = ll[j] * right_prod
            right_prod *= nums[j]

        return ll

        """
    return [x * y for (x, y) in zip(ll, rl)]
    """
    instead of zipping, we can generate the result as such (by default it returns a generator, so have to turn it into a list of lists and return the first element)
    res.append(list(ll[i] * rl[i] for i in range(len(nums))))
    return res[0]
    """


def productExceptSelf_space_efficient(nums):  # O(N) and O(1)
    length = len(nums)
    answer = [0]*length
    answer[0] = 1
    for i in range(1, length):
        # answer[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all 
        # elements to the left of index 'i'
        answer[i] = nums[i - 1] * answer[i - 1]
    # R contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R would be 1
    R = 1;
    for i in reversed(range(length)):
        # For the index 'i', R would contain the 
        # product of all elements to the right. We update R accordingly
        answer[i] = answer[i] * R
        R *= nums[i]
    return answer

if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
    print(productExceptSelf_space_efficient([1, 2, 3, 4]))
