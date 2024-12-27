"""
You are given two sets, list1 and list2, each represented as a list.
These sets can contain words (strings) or nested sets (lists of words or other sets).
Your task is to implement a function areSetsEqual that checks if the two sets are equal, considering their content and structure.

Equality Definition:
Two sets are considered equal if they contain the same string elements, regardless of order.
Sets can contain nested sets.

Normalize Sets:
Convert both sets into a canonical form where:
    Strings are stored as they are.
    Nested sets are recursively sorted and compared.
Recursive Comparison:
    Compare individual elements.
    If both elements are nested sets, recursively call the function to check their equality.
Sorting:
    Sort the elements within each set to ensure that order does not matter.
"""
def areSetsEqual(list1, list2):
    def normalize_set(s):
        """
        O(nlogn)
        O(n+d)
        n total number of elements (incl nested elements) in both lists
        m is the size of the current list
        Normalize the set by sorting its elements and recursively processing nested sets.
        """
        normalized = []
        for item in s:
            if isinstance(item, list): # used to check if an object is an instance of a specified class or a tuple of classes
                normalized.append(normalize_set(item))  # Recursively normalize nested sets
            else:
                normalized.append(item)  # Strings are added directly
        return sorted(normalized, key=lambda x: (isinstance(x, list), x))
    
    return normalize_set(list1) == normalize_set(list2)
