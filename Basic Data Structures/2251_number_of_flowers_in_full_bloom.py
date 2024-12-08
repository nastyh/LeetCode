class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """
        O(nlogn) and O(N)
        sort flowers by start and end times
        count how many flowers are blooming at a time that works for each person
        Get a list of counts for each peson 
        
        sort and save in two different lists 
        iterate over people 
        find the rightmost and leftmost indices where people[i]
        can be inserted between flowersStartTime and flowersEndTime without disrupting their sorted order.
        Diff between the indices the number of blooming flowers matching a person
        update people[i]
        return
        """
        flowersStartTime = sorted(startTime for startTime, endTime in flowers)
        flowersEndTime = sorted(endTime for startTime, endTime in flowers)
        for i in range(len(people)):
            rightIndex =  bisect_right(flowersStartTime, people[i]) 
            leftIndex = bisect_left(flowersEndTime, people[i])
            people[i] = rightIndex - leftIndex

        return people

        def fullBloomFlowers_helper(self, flowers: List[List[int]], people: List[int]) -> List[int]:
            """
            Same as above but implemented bisect manually 
            """
            def _helper_most_right(value, nums):
                l , r = 0, len(nums) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if nums[m] <= value:
                        l = m + 1 # can insert at or after m + 1
                    else:
                        r = m - 1 # insert before mid 
                return l
            
            def _helper_most_left(value, nums):
                l , r = 0, len(nums) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if nums[m] < value:
                        l = m + 1 # should insert after m
                    else:
                        r = m - 1 # at m or before
                return l 

            flowersStartTime = sorted(startTime for startTime, endTime in flowers)
            flowersEndTime = sorted(endTime for startTime, endTime in flowers)
            for i in range(len(people)):
                rightIndex =  _helper_most_right(people[i], flowersStartTime) 
                leftIndex = _helper_most_left(people[i], flowersEndTime)
                people[i] = rightIndex - leftIndex

            return people