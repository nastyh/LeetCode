class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        O(m + n) probably both
        take arr1, process each number there as a string
        keep building current_str
        example: arr1 = [1, 10, 100]
        it becomes: {1: 0} after processing 1
        then it becomes {1:1} after processing the 1 in 10 
        then it becomes {1:1, 10: 0} after processing the whole 10
        then it becomes {1:2, 10:0} after processing the 1 in 100
        then it becomes {1: 2, 10:1, 100:0}
        iterate over arr2 
        we check every candidate whether it exists in d: if so: update str2
        It will be the best line we can build. The longest variant is the answer 
        """
        d, res = {}, 0
        for i in range(len(arr1)):
            str1 = ''
            for j in str(arr1[i]):
                str1 += j
                if str1 not in d:
                    d[str1] = 0
                else: d[str1] += 1
        print(f"after building out d: {d}")
        for k in range(len(arr2)):
            str2 = ''
            for n in str(arr2[k]):
                str2 += n 
                if str2 in d:
                    res = max(res, len(str2))
        return res