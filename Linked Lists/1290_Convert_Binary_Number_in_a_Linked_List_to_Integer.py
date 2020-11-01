def getDecimalValue(head):  # O(N) both 
    """
    traverse the linked list, save the values to a list
    Using the helper function, convert to a decimal number
    """
    if not head: return 0
    def _helper(nums):
        return sum([2 ** k if v == 1 else 0 for k, v in enumerate(list(reversed(nums)))])
    collect = []
    while head:
        collect.append(head.val)
        head = head.next
    return _helper(collect)


def getDecimalValue_bits(head):  # O(n) and O(1)
    """
    Inititalize res with the head value
    Then start iterating through the rest of the list: double what's already in res and add the current node's value
    Saves space as a result
    """
    res = head.val
    while head:
        if head.next: res = res * 2 + head.next.val
        head = head.next
    return res