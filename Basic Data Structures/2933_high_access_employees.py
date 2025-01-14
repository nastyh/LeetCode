from collections import defaultdict
from typing import List


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        """
        O(mnlogn), m employees, n num of accesses to each employee
        O(mn) for the defaultdict 
        """
        d = defaultdict(list)
        res = []
        for emp, time in access_times:
            d[emp].append(time) # emp: [all their times]
        
        def _helper(times):
            """
            takes a list like ["0549", "0617", "0800"]
            compares ith with i+1th
            If the diff < 60, means more than one access in the last 60 min 
            If more than 3 of such, True 
            Else, False 
            """
            n = len(times)
            for i in range(n):
                """
                Say "0549"
                Hour part is 05 --> 5
                Min part is 49 
                Hour * 60 is minutes
                Above minutes from original minutes
                Overall we get a total number of minutes since the midnight 
                """
                start_time = int(times[i][:2]) * 60 + int(times[i][2:])
                count = 1
                for j in range(i + 1, n):
                    end_time = int(times[j][:2]) * 60 + int(times[j][2:])
                    if end_time - start_time < 60:
                        count += 1
                    else:
                        break
                if count >= 3:
                    return True
            return False

        for emp, times in d.items():
            times.sort() # by starting time 
            if _helper(times): # throw a list of times for each employee
                # if 3 or more accesses, add to res 
                res.append(emp)
        return res 