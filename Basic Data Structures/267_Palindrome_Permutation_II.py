from collections import Counter
def generatePalindromes(s):
    if not s:
        return [""]
    # preprocess
    countS = Counter(s)
    odd = False
    chars = ''
    pivot = ''
    for k, v in countS.items():
        if v % 2 == 0:
            chars += k * (v//2)
        elif v == 1 and not odd:
            pivot = k
            odd = True
            continue
        elif v % 2 != 0 and not odd:
            pivot = k
            chars += k*(v // 2)
            odd = True
        elif v % 2 != 0 and odd:
            return []
    def permute(path, visited):
        if len(path) == (len(s)//2):
            if pivot:
                res.append(path[::-1] + pivot + path)
            else:
                res.append(path[::-1] + path)
            return
        else:
            for i in range(len(chars)):
                if visited[i] or (i > 0 and chars[i] == chars[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = True
                permute(path + chars[i], visited)
                visited[i] = False
    res = []
    visited = [False] * (len(s) // 2)
    permute('', visited)
    return res


def generatePalindromes_alt(s):  # works but quickly times out. O((n + 1)!) and O(n)
    """
    Brute force approach:
    Generate all permutations (_permutations() does it, taking care of repeat characters by doing sorting)
    Then go one by one and check if it's a palindrome 
    """
    ans = []
    d = Counter(s)
    if sum([1 for v in d.values() if v % 2 == 1]) > 1: return []
    def _isPal(string):
        return string == string[::-1]
    def _permutations(st):
        res = []
        l = len(st)
        def _helper(string, curr_res):
            string = "".join(sorted(string))
            if len(curr_res) == l:
                res.append(curr_res[:])
            for i in range(len(string)):
                if i > 0 and string[i] == string[i - 1]:
                    continue
                _helper(string[:i] + string[i + 1:], curr_res + string[i])
        _helper(st, '')
        return res
    all_possible = _permutations(s)
    for candidate in all_possible:
        if _isPal(candidate):
            ans.append(candidate)
    return ans

if __name__ == '__main__':
    # print(generatePalindromes('aabb'))
    print(generatePalindromes_alt('aabb'))
    # print(generatePalindromes_alt('aabbhijkkjih'))  # takes a lot of time to run