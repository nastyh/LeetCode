class Solution:
    def nextClosestTime(self, time: str) -> str:
        """
        O(1) both 
        since all the lists have 60 elements at most 
        so double loops and sorting don't matter
        Digits to work with into digits
        Build all potential numbers 
        if a number < 24, it can be an hour candidate
        if a number < 59, it can be a minute candidate
        """
        digits = []
        for t in time: 
            if t.isdigit(): digits.append(t)

        hours_candidates = []
        minutes_candidates = []

        digits.sort() 
        for d1 in digits:
            for d2 in digits:
                pair = d1 + d2
                if int(pair) < 24: hours_candidates.append(pair)
                elif int(pair) < 59: minutes_candidates.append(pair)

        HH, MM = time.split(':')
        # looking for the next number that is larger than what we work with
        for pair in hours_candidates: # since it's sorted 
            if pair > MM: return HH + ':' + pair
        for pair in minutes_candidates:
            if pair > MM: return HH + ':' + pair
        MM = hours_candidates[0] # min value from this list

        for pair in hours_candidates:
            if pair > HH: return pair + ':' + MM
        HH = hours_candidates[0] # min value from this list
        return HH + ':' + MM 