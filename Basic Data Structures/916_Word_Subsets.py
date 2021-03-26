from collections import Counter
def wordSubsets(A, B):  # O(A + B) both
    maxB = Counter()
    for b in B:
        temp = Counter(b)
        for key in temp:
            maxB[key] = max(maxB.get(key, 0), temp[key])
    ans = []
    for a in A:
        # is maxB subset of me?
        temp = Counter(a)
        subset = True
        for key in maxB:
            if key not in temp or (key in temp and temp[key] < maxB[key]):
                subset = False
        if subset:
            ans.append(a)
    return ans  


if __name__ == '__main__':   
    print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))