class Solution:
    def average(self, salary: List[int]) -> float:
        """
        O(n) and O(1)
        track curr_min and curr_max so we can eventually find the smallest and
        the largest elements respectively
        Then subtract them and divide by the len minus 2
        """
        curr_min, curr_max = math.inf, -math.inf
        res = 0
        for s in salary:
            curr_min = min(curr_min, s)
            curr_max = max(curr_max, s)
            res += s 
        return (res - curr_min - curr_max) / (len(salary) - 2) # key is to use / and not //

    def average_sort(self, salary: List[int]) -> float:
        """
        O(nlogn) and O(1)
        sort, take from the second to the second last 
        divide by len minus 2
        Works b/c all the elements are unique
        """
        salary.sort()
        res = 0
        for ix in range(1, len(salary) - 1):
            res += salary[ix]
        return res / (len(salary) - 2)

    def average_one_liner(self, salary: List[int]) -> float:
        """
        prob O(nlogn) for using min/max
        O(1)
        """
        return(sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
