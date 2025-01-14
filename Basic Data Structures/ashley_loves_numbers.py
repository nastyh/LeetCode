"""
Given a range of Numbers, Find the Numbers with No DIGIT Repeated (Both Numbers Inclusive)
"""
def find_numbers_with_unique_digits(start, end):
    """
    O(nlogn) due to going via range and doing sets, it's proportional
    to log10(n), where n=max(range)
    O(d+k), d max num of digits in the nums, k count of valid numbers 
    """
    def has_unique_digits(number):
        digits = str(number)
        return len(digits) == len(set(digits))  # Check if digits are unique

    result = [num for num in range(start, end + 1) if has_unique_digits(num)]
    return result

