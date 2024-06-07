class Solution:
    def compareVersion(self, version1: str, version2: str) -> int: # O(n) both
        # get rid of the dots
        # v1 and v2 are lists of strings of numbers 
        v1, v2 = version1.split("."), version2.split(".")
        i, j = len(v1) - 1, len(v2) - 1
        # get rid of the zeroes
        while v1 != [] and int(v1[i]) == 0: # while it's not the end 
            v1.pop()
            i -= 1
        while v2 != [] and int(v2[j]) == 0: # while it's not the end 
            v2.pop()
            j -= 1
        for i in range(len(min(v1, v2))):
            int1, int2 = int(v1[i]), int(v2[i])
            # based on the question
            if int1 > int2:
                return 1
            elif int1 < int2:
                return -1
        if len(v1) > len(v2):
            return 1
        elif len(v2) > len(v1):
            return -1
        return 0