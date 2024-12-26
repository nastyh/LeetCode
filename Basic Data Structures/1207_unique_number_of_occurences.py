class Solution:
    def uniqueOccurrences_easiest(self, arr: List[int]) -> bool:
        """
        O(n) both 
        count using Counter
        go over values in the dict
        if we've such such a number, False
        otherwise, add to the set and keep processing 
        """
        d = Counter(arr)
        s = set()
        for v in d.values():
            if v not in s:
                s.add(v)
            else: return False
        return True 

    def uniqueOccurrences_pythonic(self, arr: List[int]) -> bool:
        """
        Same idea, slightly differently implemented
        len of the list of values should be == to the len of the set 
        meaning there a no repetitions 
        """
        d = Counter(arr)
        values_from_dict = [v for v in d.values()]
        set_values = list(set(values_from_dict))
        return len(values_from_dict) == len(set_values)